import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import numpy as np

# --- 1. KONFIGURACJA STRONY HTML ---
st.set_page_config(
    page_title="Solar ROI Calculator",
    page_icon="☀️",
    layout="wide"
)

# Tytuł i opis na stronie
st.title("☀️ Solar Invest: Analiza Opłacalności Fotowoltaiki")
st.markdown("""
Ta aplikacja łączy **dane satelitarne (Open-Meteo)** z modelem finansowym, 
aby obliczyć zwrot z inwestycji w dowolnym miejscu na Ziemi.
""")

# --- 2. FUNKCJE (BACKEND) ---
def get_solar_data(lat, lon):
    try:
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": "2022-01-01",
            "end_date": "2022-12-31",
            "daily": "shortwave_radiation_sum",
            "timezone": "auto"
        }
        r = requests.get(url, params=params)
        data = r.json()
        # Przeliczenie MJ -> kWh
        return (np.array(data['daily']['shortwave_radiation_sum']) * 0.277).sum()
    except:
        return 0

def calculate_roi(production, cost, price, inflation, years=15):
    cash_flow = [-cost]
    curr_price = price
    for _ in range(years):
        saving = production * curr_price
        cash_flow.append(cash_flow[-1] + saving)
        curr_price *= (1 + inflation/100)
    return pd.DataFrame({"Rok": range(years+1), "Bilans": cash_flow})

# --- 3. PASEK BOCZNY (INPUTY) ---
with st.sidebar:
    st.header("⚙️ Parametry Inwestycji")
    power = st.number_input("Moc instalacji (kWp)", value=5.0, step=0.5)
    cost = st.number_input("Koszt instalacji (PLN)", value=25000)
    price = st.slider("Cena energii (PLN/kWh)", 0.5, 2.0, 0.9)
    inflation = st.slider("Inflacja energii (%)", 0, 20, 10)
    st.info("Kliknij na mapie, aby pobrać dane dla lokalizacji!")

# --- 4. GŁÓWNY WIDOK (MAPA + WYKRESY) ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📍 Wybór lokalizacji (GIS)")
    # Tworzymy mapę
    m = folium.Map(location=[52.0, 19.0], zoom_start=6)
    folium.LatLngPopup().add_to(m)
    
    # Wyświetlamy mapę i pobieramy kliknięcie
    map_output = st_folium(m, height=400, width=None)

# Sprawdzamy, czy użytkownik kliknął mapę
if map_output['last_clicked']:
    lat = map_output['last_clicked']['lat']
    lon = map_output['last_clicked']['lng']
    
    with col2:
        st.subheader("📊 Wyniki Analizy")
        with st.spinner('Pobieram dane satelitarne...'):
            # Logika biznesowa
            rad = get_solar_data(lat, lon)
            prod = rad * power * 0.8
            df = calculate_roi(prod, cost, price, inflation)
            profit = df["Bilans"].iloc[-1]
            
            # Wyświetlanie metryk (duże liczby)
            m1, m2 = st.columns(2)
            m1.metric("Nasłonecznienie", f"{rad:.0f} kWh/m²")
            m2.metric("Produkcja", f"{prod:.0f} kWh/rok")
            
            st.metric("Zysk po 15 latach", f"{profit:,.0f} PLN", 
                      delta="Opłacalne" if profit > 0 else "Nieopłacalne")
            
            # Wykres liniowy
            st.line_chart(df.set_index("Rok"))
else:
    with col2:
        st.info("👈 Wybierz punkt na mapie po lewej stronie.")