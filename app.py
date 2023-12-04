# STREAMLIT DEMO

import streamlit as st
import time

# Titles, headers, subheaders
st.title("To jest tytuł aplikacji")
st.header("To jest nagłówek")
st.subheader("To jest nagłówek podrzędny")
st.text("To jest tekst")
st.markdown("To jest `markdown`")
st.markdown("### To jest Nagłówek 3 w markdown")
st.text("To jest wzór:")
st.latex(r"e^{i\pi} + 1 = 0")  ## to jest wzór
st.text(
    body="To jest tekst z adnotacją, najedź myszą",
    help="Adnotacja"
    )
st.text("Kod w pythonie")
st.code(body="print('Hello World')", language="python")

# Informations
st.header("Informacje")
st.info("To jest informacja")
st.warning("To jest ostrzeżenie")
st.success("To jest sukces")
st.error("To jest błąd")

# Input
st.header("Wprowadzanie danych")
st.text_input(label="To jest pole tekstowe")
st.text_input(label=":book: Możemy używać emotikonów :smile:")
st.number_input(
    label="To jest wprowadzanie numeru. Ile masz lat?",
    value=0,
    help="To jest pomoc",
    min_value=0,
    max_value=125,
    step=10,  # krok co 10
)
st.checkbox(label="To jest checkbox")

# Input with variable assignment
st.header("Przypisanie wartości do zmiennej")
var1 = st.multiselect(
    "Wybór wielokrotny",
    options=["pies", "kot", "mysz"]
    )
var2 = st.selectbox(
    "Wybór jednokrotny",
    options=["pies", "kot", "mysz"]
    )
st.text(f"W polu 1 wybrałeś: {var1}")
st.text(f"W polu 2 wybrałeś: {var2}")

# Columns
st.header("Kontrolki w kolumnach")
col1, col2 = st.columns(2)
var3 = col1.selectbox(
    "Ulubiony zespół",
    options=["Dire Straits", "Manowar", "Pink Floyd"]
    )
var4 = col2.selectbox(
    "Ulubione jedzenie",
    options=["Pizza", "Kebab", "Burger"]
    )

# The same with expander
st.header("Ekspander")
with st.expander("Kliknij aby rozwinąć"):
    col3, col4 = st.columns(2)
    var5 = col3.selectbox(
        "Ulubiona epoka",
        options=["lata 30", "lata 50", "lata 80"]
        )
    var6 = col4.selectbox(
        "Ulubione danie chińskie",
        options=["Chop suey", "Gong bao", "Bao"]
        )

    st.write(f"Ulubiona epoka: {var5}")
    st.write(f"Ulubione danie chińskie: {var6}")

    # The primary button retunr True if clicked
    btn = st.button(label="Zapisz", type="primary")
    if btn:
        with st.spinner("Zapisuję..."):
            time.sleep(5)  # Simulate saving
            st.success("Zapisano!")
            st.snow()
            time.sleep(3)
            st.rerun()

