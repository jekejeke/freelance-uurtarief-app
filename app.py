import streamlit as st
import pandas as pd

st.title("Freelance Uurtarief Vergelijker")

# Lees het Excel-bestand in
excel_path = "uurtarief_totaal.xlsx"
df = pd.read_excel(excel_path)

# Selecteer Profession
professions = pd.Series(df['Profession']).dropna().unique()
profession = st.selectbox("Kies je beroepsgroep (Profession):", sorted(professions))

# Filter specialisaties op gekozen Profession
specializations = pd.Series(df[df['Profession'] == profession]['Specialization']).dropna().unique()
specialization = st.selectbox("Kies je specialisatie (Specialization):", sorted(specializations))

# Filter de juiste rij uit de dataset
row = df[(df['Profession'] == profession) & (df['Specialization'] == specialization)]

if not row.empty:
    gemiddelde = float(row.iloc[0]['Average Hourly Rate'])
    # Check of profession en specialization strings zijn voordat we lower() aanroepen
    prof_str = profession.lower() if isinstance(profession, str) else str(profession)
    spec_str = specialization.lower() if isinstance(specialization, str) else str(specialization)
    st.write(f"Gemiddeld uurtarief voor {prof_str} ({spec_str}): €{gemiddelde}")
    
    # Voer eigen uurtarief in
    uurtarief = st.number_input("Wat is jouw uurtarief? (€)", min_value=0.0, step=1.0)
    
    # Vergelijking
    if uurtarief > 0:
        verschil = uurtarief - gemiddelde
        procent = (verschil / gemiddelde) * 100
        if verschil > 0:
            st.success(f"Je zit €{verschil:.2f} ({procent:.1f}%) boven het gemiddelde!")
        elif verschil < 0:
            st.warning(f"Je zit €{abs(verschil):.2f} ({abs(procent):.1f}%) onder het gemiddelde.")
        else:
            st.info("Je zit precies op het gemiddelde!")
else:
    st.error("Geen data gevonden voor deze combinatie van beroepsgroep en specialisatie.") 