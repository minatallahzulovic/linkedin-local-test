# LinkedIn Local Testing Project

## 📌 Opis projekta

Projekt predstavlja automatizirano testiranje ključnih funkcionalnosti LinkedIn aplikacije. Testovi su izvršavani **lokalno** na računaru korištenjem Selenium WebDriver-a, zbog LinkedIn-ove CAPTCHA zaštite koja onemogućava testiranje putem cloud platformi.

## 📊 Rezultati testiranja

| Status | Broj testova | Procenat |
|--------|--------------|----------|
| ✅ PASSED | 14 | 93.3% |
| ❌ FAILED | 1 | 6.7% |
| **UKUPNO** | **15** | **100%** |

### Detaljni rezultati

| Test | Naziv | Status |
|------|-------|--------|
| TC_01 | Homepage title | ✅ PASSED |
| TC_02 | Homepage load | ✅ PASSED |
| TC_03 | Login page email field | ✅ PASSED |
| TC_04 | Login page password field | ✅ PASSED |
| TC_05 | Login button exists | ✅ PASSED |
| TC_06 | Positive login | ✅ PASSED |
| TC_07 | Negative login - wrong password | ✅ PASSED |
| TC_08 | Negative login - empty email | ✅ PASSED |
| TC_09 | Negative login - empty password | ✅ PASSED |
| TC_10 | Forgot password link | ✅ PASSED |
| TC_11 | Jobs page access | ✅ PASSED |
| TC_12 | Job search | ❌ FAILED |
| TC_13 | Profile icon exists | ✅ PASSED |
| TC_14 | HTTPS usage | ✅ PASSED |
| TC_15 | Footer links | ✅ PASSED |

### Analiza palog testa

**TC_12 (Job search)** – pao je zbog LinkedIn-ove dinamičke promjene XPath atributa za polje za pretragu. Ovo je dokumentovano kao bug.

## 🛠️ Korišteni alati

| Alat | Namjena |
|------|----------|
| Selenium WebDriver | Automatizacija web aplikacija |
| pytest | Framework za izvršavanje testova |
| webdriver-manager | Automatsko upravljanje ChromeDriver-om |
| Python | Programski jezik |

## 🚀 Upute za pokretanje

### 1. Kloniraj repozitorij
git clone https://github.com/minatallahzulovic/linkedin-local-test.git
cd linkedin-local-test

### 2. Instaliraj potrebne biblioteke
pip install -r requirements.txt

### 3. Pokreni testove
python -m pytest test_linkedin_local.py -v -s

### 📁 Struktura repozitorija

linkedin-local-test/
│
├── test_linkedin_local.py      # Glavni fajl sa 15 testova
├── requirements.txt             # Potrebne biblioteke
└── README.md                    # Opis projekta

### 👤 Autor
Minatallah Zulović

### 📅 Datum
24.04.2026.


```bash
git clone https://github.com/minatallahzulovic/linkedin-local-test.git
cd linkedin-local-test
