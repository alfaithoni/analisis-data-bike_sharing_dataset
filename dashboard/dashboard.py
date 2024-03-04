import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

current_dir = os.path.dirname(__file__)

st.title("Analisis Data Bike Sharing Dataset")

with st.sidebar:
    st.write("Bike sharing dataset merupakan dataset yang berisikan data terkait proses persewaan sepeda di Washington DC pada tahun 2011-2012. Dataset ini menjadi menarik karena memiliki korelasi dengan kondisi lingkungan dan musim yang ada. Karakteristik dataset ini menarik untuk digunakan dalam baik pembelajaran maupun penelitian. Dataset ini dapat menggambarkan kondisi mobilitas pada sebuah kota.")
    st.write("Nama              : Muhammad Hanif Al Faithoni")
    st.write("Email             : hanifalfaithoni@gmail.com | m002d4ky2849@bangkit.academy")
    st.write("Username Dicoding : nipanip")
    
# Load data csv
total_per_season_df = pd.read_csv(os.path.join(current_dir,"total_per_season.csv"))


# Visualisasi data
tab1 = st.tabs(["Hasil Analisis 1"])
with tab1:
    total_per_season_df.set_index('season', inplace=True)
    plt.figure(figsize=(8, 5))
    total_per_season_df.plot(kind='bar', color=["#72BCD4", "#72BCD4", "#D3D3D3", "#D3D3D3"])
    plt.title('Total Bike Rentals by Season')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    st.pyplot(plt)