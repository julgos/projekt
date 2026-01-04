import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import numpy as np

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Solar Invest",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS - DESIGN SYSTEM ---
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    
    /* Karty KPI */
    div[data-testid="stMetric"] {
        background-color: #F8FDFF;
        border: 1px solid #D1E9FF;
        border-left: 5px solid #0066CC;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    h1, h2, h3, h4, h5 { color: #004080; font-family: 'Helvetica Neue', sans-serif; }
    section[data-testid="stSidebar"] { background-color: #F0F7FF; border-right: 1px solid #CCE5FF; }
    div[data-testid="stSlider"] label { font-weight: bold; color: #0066CC; }

    .sidebar-title {
        text-align: center;
        font-weight: bold;
        font-size: 24px;
        color: #004080;
        margin-bottom: 20px;
    }
    
    .stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 3. BACKEND (LOGIKA BIZNESOWA) ---
def get_solar_data(lat, lon):
    try:
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": lat, "longitude": lon,
            "start_date": "2022-01-01", "end_date": "2022-12-31",
            "daily": "shortwave_radiation_sum", "timezone": "auto"
        }
        r = requests.get(url, params=params)
        data = r.json()
        return (np.array(data['daily']['shortwave_radiation_sum']) * 0.277).sum()
    except:
        return 0

def calculate_roi_advanced(start_production, cost, price_buy, price_sell, inflation, auto_consumption, years=30):
    cash_flow = [-cost]
    cumulative_cash = [-cost]
    
    current_price_buy = price_buy
    current_price_sell = price_sell
    
    degradation_rate = 0.005  
    opex_yearly = 150         
    
    for year in range(1, years + 1):
        year_prod = start_production * (1 - (degradation_rate * (year - 1)))
        
        used = year_prod * (auto_consumption / 100)
        sold = year_prod - used
        
        savings = used * current_price_buy
        earnings = sold * current_price_sell
        total = savings + earnings - opex_yearly
        
        cash_flow.append(total)
        cumulative_cash.append(cumulative_cash[-1] + total)
        
        current_price_buy *= (1 + inflation/100)
        current_price_sell *= (1 + inflation/100)
    
    return pd.DataFrame({"Rok": range(0, years + 1), "Bilans": cumulative_cash})

# --- 4. SIDEBAR ---
with st.sidebar:
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        st.image("https://cdn.pixabay.com/photo/2022/06/07/13/22/weather-7248402_1280.png", width=90)
    
    st.markdown('<div class="sidebar-title">Solar Invest</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    with st.expander("1. Parametry Instalacji", expanded=True):
        # --- ZMIANA: Podajemy powierzchnię, obliczamy moc ---
        roof_area = st.number_input("Dostępna powierzchnia dachu (m²)", value=30, step=5)
        
        # Przelicznik: 1 kWp zajmuje ok. 5.2 m2
        power_calculated = roof_area / 5.2
        
        # Wyświetlamy wynik obliczeń na niebiesko
        st.info(f"⚡ Możliwa moc instalacji: **{power_calculated:.2f} kWp**")
        
        # Koszt nadal podajemy ręcznie, ale z podpowiedzią
        estimated_market_cost = power_calculated * 4500 # Średnio 4500 zł za kWp
        
        cost = st.number_input("Koszt inwestycji (PLN)", value=25000, step=1000, 
                               help=f"Rynkowy koszt dla {power_calculated:.1f} kWp to ok. {estimated_market_cost:,.0f} zł")
        
        st.caption(f"Sugerowany koszt rynkowy: ok. {estimated_market_cost:,.0f} PLN")
        
        auto_rate = st.slider("Autokonsumpcja (%)", 0, 100, 25, help="Ile energii zużywasz na bieżąco?")

    with st.expander("2. Parametry Rynku", expanded=False):
        price_buy = st.number_input("Cena zakupu (PLN)", value=1.10, step=0.01)
        price_sell = st.number_input("Cena sprzedaży (PLN)", value=0.50, step=0.01)
        inflation = st.slider("Inflacja (%)", 0, 20, 10)
        
    st.markdown("---")
    
    st.subheader("Twój Cel")
    user_years = st.slider("Horyzont analizy (lata)", min_value=1, max_value=30, value=12)
    st.caption(f"Sprawdzamy zysk po {user_years} latach.")
    
    st.info("👇 Wybierz styl mapy i kliknij lokalizację!")

# --- 5. GŁÓWNY WIDOK ---
st.subheader(f"🗺️ Analiza Rentowności (Perspektywa: {user_years} lat)")

col_map, col_results = st.columns([1.3, 1], gap="large")

# --- LEWA KOLUMNA: MAPA ---
with col_map:
    map_style = st.radio(
        "Wybierz widok mapy:",
        ["Standardowa", "Satelitarna", "Jasna"], 
        horizontal=True
    )
    
    if map_style == "Standardowa":
        tiles_url, attr = "OpenStreetMap", None
    elif map_style == "Satelitarna":
        tiles_url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
        attr = "Esri"
    else:
        tiles_url, attr = "CartoDB positron", None

    m = folium.Map(location=[52.0, 19.0], zoom_start=6, tiles=tiles_url, attr=attr)
    folium.LatLngPopup().add_to(m)
    map_output = st_folium(m, height=480, width=None)

    lat, lon = None, None
    if map_output['last_clicked']:
        lat = map_output['last_clicked']['lat']
        lon = map_output['last_clicked']['lng']
        
        with st.spinner('Pobieranie danych satelitarnych...'):
            rad = get_solar_data(lat, lon)
            # Używamy Mocy Wyliczonej z Powierzchni (power_calculated)
            prod_start = rad * power_calculated * 0.82 
            
            st.markdown("###### ☀️ Warunki lokalne:")
            c1, c2 = st.columns(2)
            c1.metric("Nasłonecznienie", f"{rad:.0f} kWh/m²")
            c2.metric("Produkcja roczna", f"{prod_start:.0f} kWh")

# --- PRAWA KOLUMNA: WYNIKI ---
with col_results:
    if lat:
        # Obliczenia z nową mocą
        df = calculate_roi_advanced(prod_start, cost, price_buy, price_sell, inflation, auto_rate, years=30)
        
        custom_result = df[df['Rok'] == user_years]['Bilans'].values[0]
        break_even = df[df['Bilans'] >= 0]
        year_be = break_even['Rok'].min() if not break_even.empty else None
        
        st.markdown(f"##### 📊 Twój Wynik Finansowy")
        
        k1, k2 = st.columns(2)
        delta_color = "normal" if custom_result > 0 else "inverse"
        
        k1.metric(f"Wynik finansowy z inwestycji po {user_years} latach", 
                  f"{custom_result:,.0f} PLN", 
                  delta="Zysk/Strata netto", delta_color=delta_color)
        
        if year_be:
            k2.metric("Zwrot inwestycji", f"{year_be}. rok", delta="Break-even point")
        else:
            k2.metric("Zwrot inwestycji", "> 30 lat", delta="Brak zwrotu", delta_color="inverse")
            
        st.markdown("---")
        st.markdown("###### Symulacja Cash Flow (30 lat)")
        st.area_chart(df.set_index("Rok")['Bilans'], color=["#0066CC"])
        
        if custom_result > 0:
            st.success(f"✅ Inwestycja rentowna w horyzoncie {user_years} lat.")
        else:
            st.warning(f"⚠️ Inwestycja nie zwróci się w ciągu {user_years} lat.")

    else:
        st.info("👈 Wybierz lokalizację na mapie, aby rozpocząć.")
        st.markdown("""
        **Instrukcja:**
        1. Podaj parametry wejściowe:
        - *Dostępna powierzchnia dachu* - system automatycznie obliczy maksymalną moc instalacji.
        - *Koszt inwestycji* - wpisz kwotę (system podpowie wartość rynkową).
        - *Parametry rynku* - ceny energii i autokonsumpcja.
        2. Wybierz Twój cel zwrotu inwestycji w latach.
        3. Zaznacz na mapie lokalizację (użyj widoku satelitarnego, aby trafić w dach).
        """)