# Freelance Uurtarief Vergelijker

Deze webapplicatie helpt freelancers hun eigen uurtarief te vergelijken met het gemiddelde uurtarief per beroepsgroep en specialisatie, op basis van een aangeleverde dataset.

## Functionaliteit
- Kies je beroepsgroep (Profession) en specialisatie (Specialization)
- Vul je eigen uurtarief in
- Zie direct of je boven of onder het gemiddelde zit, en met hoeveel

## Benodigdheden
- Python 3
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)

Installeer de dependencies met:
```bash
pip install -r requirements.txt
```

## Dataset
Plaats een Excel-bestand `uurtarief_totaal.xlsx` in de projectmap met minimaal de volgende kolommen:
- `Profession`
- `Specialization`
- `Average Hourly Rate`
- `Year`

## Starten van de app
```bash
streamlit run app.py
```

De app is dan bereikbaar op [http://localhost:8501](http://localhost:8501)

## Voorbeeld
![screenshot](screenshot.png)

---
Vragen of suggesties? Maak een issue aan of stuur een pull request! 