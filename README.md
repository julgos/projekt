# Solar Invest - System Analizy Rentowności PV

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=leaflet&logoColor=white)
![Open-Meteo](https://img.shields.io/badge/API-Open--Meteo-orange?style=for-the-badge)

## O projekcie
**Solar Invest** jest aplikacją webową wspierającą analizę opłacalności inwestycji w instalacje fotowoltaiczne dla użytkowników indywidualnych. System umożliwia przeprowadzenie symulacji finansowej na podstawie rzeczywistych danych nasłonecznienia, parametrów technicznych instalacji oraz zmiennych rynkowych, takich jak ceny energii elektrycznej czy poziom inflacji.
Głównym celem aplikacji jest dostarczenie użytkownikowi prostego i intuicyjnego narzędzia decyzyjnego, które pozwala oszacować roczną produkcję energii, skumulowany bilans finansowy oraz punkt zwrotu inwestycji w zadanym horyzoncie czasowym. Aplikacja wykorzystuje interaktywną mapę do wyboru lokalizacji inwestycji oraz prezentuje wyniki analizy w postaci kluczowych wskaźników efektywności (KPI) i wykresu cash flow, co umożliwia szybkie i czytelne porównanie opłacalności inwestycji.

---
## 2. Prawa autorskie

**Autorzy:**  
Julia Goska  
Aleksandra Buńko  

**Warunki licencyjne:**  
Oprogramowanie udostępniane jest na licencji otwartej MIT. Licencja ta umożliwia dalsze wykorzystanie, modyfikację oraz rozwój kodu źródłowego, w szczególności w celach edukacyjnych i akademickich, z zachowaniem informacji o autorach.

---
## 3. Specyfikacja Wymagań
| ID | Nazwa wymagania | Opis wymagania | Priorytet | Kategoria |
|----|-----------------|----------------|-----------|-----------|
| 1 | Konfiguracja aplikacji webowej | System działa jako aplikacja webowa z responsywnym interfejsem użytkownika | 1 | Pozafunkcjonalne |
| 2 | Czytelność interfejsu | Interfejs jest spójny wizualnie i czytelny dla użytkownika | 2 | Pozafunkcjonalne |
| 3 | Pobieranie danych nasłonecznienia | System pobiera dane promieniowania słonecznego z zewnętrznego API (Open-Meteo) | 1 | Funkcjonalne |
| 4 | Obsługa błędów API | System zapewnia stabilne działanie w przypadku błędów komunikacji z API | 1 | Pozafunkcjonalne |
| 5 | Konwersja jednostek | System przelicza dane promieniowania do jednostek kWh/m² | 1 | Funkcjonalne |
| 6 | Symulacja cash flow | System symuluje skumulowany bilans finansowy inwestycji | 1 | Funkcjonalne |
| 7 | Uwzględnienie inflacji | System uwzględnia inflację cen energii w analizie ekonomicznej | 1 | Funkcjonalne |
| 8 | Autokonsumpcja i sprzedaż energii | System rozróżnia energię zużytą na potrzeby własne i sprzedaną do sieci | 1 | Funkcjonalne |
| 9 | Punkt zwrotu inwestycji | System wyznacza rok osiągnięcia rentowności inwestycji | 1 | Funkcjonalne |
| 10 | Degradacja paneli | System uwzględnia spadek wydajności paneli PV w kolejnych latach | 2 | Funkcjonalne |
| 11 | Sidebar konfiguracyjny | System udostępnia panel boczny do konfiguracji parametrów instalacji i rynku | 1 | Funkcjonalne |
| 12 | Obliczanie mocy instalacji | System oblicza możliwą moc instalacji na podstawie powierzchni dachu | 1 | Funkcjonalne |
| 13 | Wybór stylu mapy | System umożliwia wybór stylu mapy (standardowa, satelitarna, jasna) | 2 | Funkcjonalne |
| 14 | Interaktywna mapa | System prezentuje interaktywną mapę lokalizacji inwestycji | 1 | Funkcjonalne |
| 15 | Wybór lokalizacji | System umożliwia wybór lokalizacji poprzez kliknięcie na mapie | 1 | Funkcjonalne |
| 16 | Estymacja rocznej produkcji energii | System oblicza roczną produkcję energii instalacji PV | 1 | Funkcjonalne |
| 17 | Prezentacja kluczowych wskaźników efektywności (KPI) | System prezentuje kluczowe wskaźniki efektywności (KPI) | 1 | Funkcjonalne |
| 18 | Wykres cash flow | System wizualizuje przebieg skumulowanego bilansu finansowego | 1 | Funkcjonalne |
| 19 | Wpisanie adresu lokalizacji | System może określać dokładny adres na podstawie współrzędnych | 3 | Funkcjonalne |
| 20 | Eksport wyników do PDF | System może umożliwiać eksport wyników analizy do pliku | 3 | Funkcjonalne |

---
## 4. Architektura systemu

### 4.1 Architektura rozwoju (stos technologiczny)

- **Visual Studio Code / Jupyter Lab** – środowiska programistyczne wykorzystywane do tworzenia, testowania i analizy kodu źródłowego.
- **Python 3.12.1** – główny język programowania użyty do implementacji logiki aplikacji.
- **Biblioteki Python**:
  - `pandas` – analiza i przetwarzanie danych,
  - `numpy` – obliczenia matematyczne,
  - `requests` – obsługa komunikacji z zewnętrznym API,
  - `streamlit` – budowa interfejsu oraz wizualizacja danych,
  - `folium`, `streamlit-folium` – obsługa interaktywnej mapy.

### 4.2 Architektura uruchomieniowa

- **Streamlit 1.52.2** – framework odpowiedzialny za uruchomienie aplikacji oraz renderowanie interfejsu webowego.
- **Folium / Streamlit-Folium** – moduły odpowiedzialne za prezentację mapy oraz wybór lokalizacji inwestycji.
- **Open-Meteo API** – zewnętrzne źródło danych meteorologicznych, dostarczające dane o nasłonecznieniu w formacie JSON.
- **Aplikacja Python** – moduł obliczeniowy realizujący estymację produkcji energii oraz analizę ekonomiczną inwestycji.

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
- app2.py - Główny plik aplikacji (Production Ready).
- analiza-projekt.ipynb - Notatnik Jupyter z analizą wstępną i testami API (Development).
- requirements.txt - Lista zależności projektowych.
- .streamlit/config.toml - Konfiguracja motywu graficznego (kolory, fonty).

---

## Sceniarusze testów



| ID wymagania | Scenariusz testu | Status |
|-------------|------------------|--------|
| 1 | Uruchamiamy aplikację poleceniem `streamlit run app.py` i sprawdzamy, czy otwiera się ona w przeglądarce internetowej oraz czy widoczny jest główny widok aplikacji. | Sprawdzono |
| 3 | Klikamy na mapie kolejno lokalizacje: Warszawa, Gdańsk i Kraków, a następnie sprawdzamy, czy wyświetlane wartości nasłonecznienia różnią się między lokalizacjami. | Sprawdzono |
| 4 | Podczas standardowego działania aplikacji sprawdzamy, czy po kliknięciu lokalizacji dane są wyświetlane bez błędów i aplikacja nie przestaje działać. | Sprawdzono |
| 5 | Sprawdzamy, czy wartość nasłonecznienia wyświetlana jest w jednostkach kWh/m², zgodnie z opisem w interfejsie. | Sprawdzono |
| 6 | Po wykonaniu symulacji sprawdzamy, czy w pierwszym roku bilans finansowy jest ujemny (koszt inwestycji), a w kolejnych latach stopniowo rośnie. | Sprawdzono |
| 7 | Zmieniamy wartość inflacji w panelu bocznym na 0% i 10% i sprawdzamy, czy zmienia się wynik finansowy inwestycji. | Sprawdzono |
| 8 | Zmieniamy poziom autokonsumpcji energii i obserwujemy, czy wynik finansowy inwestycji ulega zmianie. | Sprawdzono |
| 9 | Sprawdzamy, czy aplikacja wskazuje rok, w którym bilans finansowy przechodzi z wartości ujemnej na dodatnią. | Sprawdzono |
| 11 | Sprawdzamy, czy w panelu bocznym dostępne są pola do zmiany parametrów instalacji oraz rynku energii. | Sprawdzono |
| 12 | Zmieniamy wartość dostępnej powierzchni dachu na 20 m² i 40 m² i sprawdzamy, czy obliczona moc instalacji zmienia się odpowiednio. | Sprawdzono |
| 14 | Sprawdzamy, czy mapa umożliwia przybliżanie, oddalanie oraz reaguje na kliknięcia użytkownika. | Sprawdzono |
| 15 | Klikamy wybrane miejsce na mapie i sprawdzamy, czy aplikacja oblicza dane dla tej konkretnej lokalizacji. | Sprawdzono |
| 16 | Po wyborze lokalizacji sprawdzamy, czy aplikacja wyświetla roczną produkcję energii i czy zmienia się ona po zmianie lokalizacji. | Sprawdzono |
| 17 | Sprawdzamy, czy aplikacja wyświetla wynik finansowy inwestycji oraz rok zwrotu inwestycji w formie wskaźników. | Sprawdzono |
| 18 | Sprawdzamy, czy po wykonaniu symulacji wyświetlany jest wykres przedstawiający zmianę skumulowanego bilansu finansowego w czasie. | Sprawdzono |
| 2 | Sprawdzamy, czy wszystkie elementy interfejsu są czytelne, logicznie rozmieszczone i zrozumiałe dla użytkownika. | Sprawdzono |
| 10 | Sprawdzamy, czy w kolejnych latach symulacji produkcja energii rośnie wolniej, co wskazuje na uwzględnienie spadku wydajności paneli. | Sprawdzono |
| 13 | Zmieniamy styl mapy na standardowy, satelitarny oraz jasny i sprawdzamy, czy mapa zmienia swój wygląd. | Sprawdzono |
