import streamlit as st
import pandas as pd

st.title("Załadujmy jakieś dane")

files = st.file_uploader(label="Załaduj pliki", accept_multiple_files=True)

if files:
    # Read uploaded files as pandas dataframe
    df = pd.concat([pd.read_csv(file, sep=";") for file in files])

    # Show dataframe in data editor view
    changed_df = st.data_editor(df)

    # Add button to save dataframe
    btn = st.button(label="Zapisz")

    # Save dataframe to csv file
    if btn:
        # Spinning circle animation
        with st.spinner("Zapisuję..."):
            changed_df.to_csv("changed_data.csv", sep=";", index=False)
            st.success("Zapisano!")
