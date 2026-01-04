# ☀️ Solar Invest - System Analizy Rentowności PV

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=leaflet&logoColor=white)
![Open-Meteo](https://img.shields.io/badge/API-Open--Meteo-orange?style=for-the-badge)

## O projekcie
**Solar Invest** to aplikacja typu *Rapid Data Science & GIS*, służąca do kompleksowej analizy opłacalności instalacji fotowoltaicznych w dowolnym miejscu na świecie. System integruje dane satelitarne, interaktywne mapy oraz zaawansowany model finansowy zgodny z systemem **Net-Billing**.

Projekt został zrealizowany jako część zaliczenia przedmiotu **Inżynieria Oprogramowania**. Celem było stworzenie funkcjonalnego prototypu (MVP) bez konieczności pisania dedykowanego frontendu (HTML/JS), wykorzystując podejście *Low-Code* w Pythonie.

---

## Główne Funkcjonalności

### 1. Analiza Geoprzestrzenna (GIS)
* **Interaktywna Mapa:** Wykorzystanie biblioteki `Folium` do wizualizacji lokalizacji.
* **Widok Satelitarny:** Integracja z warstwą **Esri World Imagery**, umożliwiająca precyzyjną weryfikację dachu i otoczenia (cienie, drzewa).
* **Geokodowanie:** Pobieranie współrzędnych (lat/lon) po kliknięciu myszką.

### 2. Dane Satelitarne (Backend)
* Automatyczne połączenie z **Open-Meteo API**.
* Pobieranie historycznych danych nasłonecznienia (*shortwave_radiation_sum*) dla konkretnej lokalizacji.
* Konwersja jednostek fizycznych ($MJ/m^2 \to kWh/m^2$).

### 3. Model Inżynierski i Finansowy
Aplikacja zawiera autorski algorytm `calculate_roi_advanced`, który uwzględnia realia rynkowe:
* **System Net-Billing:** Rozdzielenie ceny zakupu energii (np. 1.15 PLN) od ceny sprzedaży nadwyżek (np. 0.50 PLN).
* **Szacowanie powierzchni:** Automatyczne wyliczanie mocy instalacji na podstawie dostępnej powierzchni dachu (przelicznik $5.2 m^2/kWp$).
* **Autokonsumpcja:** Suwak pozwalający symulować procent energii zużywanej na bieżąco.
* **Cykl życia instalacji:** Uwzględnienie degradacji paneli (0.5% rocznie) oraz inflacji cen energii.

---

## Stos Technologiczny (Tech Stack)

| Komponent | Technologia | Zastosowanie |
|-----------|-------------|--------------|
| **Język** | Python 3.12 | Logika biznesowa i obliczenia |
| **Frontend** | Streamlit | Interfejs użytkownika (UI/UX) |
| **Mapy / GIS** | Folium | Wyświetlanie map i warstw satelitarnych |
| **Analiza Danych** | Pandas, NumPy | Przetwarzanie szeregów czasowych i Cash Flow |
| **Integracja API** | Requests | Komunikacja z serwerem pogodowym |

---

## Jak uruchomić projekt lokalnie?

Aby uruchomić aplikację na własnym komputerze, wykonaj następujące kroki:

1. **Sklonuj repozytorium:**
   ```bash
   git clone [https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/Solar-Invest.git](https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/Solar-Invest.git)
   cd Solar-Invest
Zainstaluj wymagane biblioteki: Zalecane jest użycie wirtualnego środowiska (venv).
Bash
pip install -r requirements.txt
Uruchom aplikację:
Bash
python -m streamlit run app2.py
Aplikacja otworzy się automatycznie w przeglądarce pod adresem http://localhost:8501.

Struktura Plików
app2.py - Główny plik aplikacji (Production Ready).
analiza-projekt.ipynb - Notatnik Jupyter z analizą wstępną i testami API (Development).
requirements.txt - Lista zależności projektowych.
.streamlit/config.toml - Konfiguracja motywu graficznego (kolory, fonty).

Autorzy
Projekt wykonany przez zespół studentów Uniwersytetu Gdańskiego:
Julia Goska
Aleksandra Buńko 
© 2026 Solar Invest Project.
