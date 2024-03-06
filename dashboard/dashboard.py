import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

current_dir = os.path.dirname(__file__)

st. set_page_config(layout="wide")

st.title("Hanif's Analisis Data Bike Sharing Dataset")

with st.sidebar:
    st.write("Bike sharing dataset merupakan dataset yang berisikan data terkait proses persewaan sepeda di Washington DC pada tahun 2011-2012. Dataset ini menjadi menarik karena memiliki korelasi dengan kondisi lingkungan dan musim yang ada. Karakteristik dataset ini menarik untuk digunakan dalam baik pembelajaran maupun penelitian. Dataset ini dapat menggambarkan kondisi mobilitas pada sebuah kota.")
    st.write("Nama              : Muhammad Hanif Al Faithoni")
    st.write("Email             : hanifalfaithoni@gmail.com | m002d4ky2849@bangkit.academy")


# Load data csv
df1 = pd.read_csv(os.path.join(current_dir,"total_per_season.csv"))
df2 = pd.read_csv(os.path.join(current_dir,"month_rent.csv"))
df3 = pd.read_csv(os.path.join(current_dir,"daystatus_rent.csv"))
df4 = pd.read_csv(os.path.join(current_dir,"hourly_rent.csv"))
df5 = pd.read_csv(os.path.join(current_dir,"hour.csv"))


# Visualisasi data
tab1, tab2, tab3, tab4, tab5= st.tabs(["Hasil Analisis 1", "Hasil Analisis 2", "Hasil Analisis 3", "Hasil Analisis 4", "Conclusion"])

with tab1:
    st.write("Musim apa penyewaan sepeda dilakukan paling banyak dan paling sedikit?")
    st.write("=> Berdasarkan hasil visualisasi data di bawah, dapat disimpulkan bahwa penyewaan sepeda paling banyak terjadi pada season Fall dan paling sedikit pada season springer")
    df1.set_index('season', inplace=True)
    plt.figure(figsize=(8, 5))
    df1.plot(kind='bar', color=["#72BCD4" , "#72BCD4", "#D3D3D3", "#D3D3D3"])
    plt.title('Total Bike Rentals By Season')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

with tab2:
    st.write("Kapan penyewaan sepeda paling banyak dan sedikit terjadi?")
    st.write("Berdasarkan visualisasi data di bawah dapat disimpulkan penyewaan sepeda paling banyak terjadi pada 15 September 2012, yaitu 8714 sepeda")
    st.write("Berdasarkan visualisasi data di bawah dapat disimpulkan penyewaan sepeda paling sedikit terjadi pada 29 Oktober 2012, yaitu 22 sepeda")
    def _plot_series(series, series_name, series_index=0):
        palette = list(sns.palettes.mpl_palette('Dark2'))
        xs = series['dteday']
        ys = series['cnt']

        plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

    fig, ax = plt.subplots(figsize=(12, 6), layout='constrained')
    df_sorted = df2.sort_values('dteday', ascending=True)
    _plot_series(df_sorted, '')
    sns.despine(fig=fig, ax=ax)
    plt.xlabel('dteday')
    plt.ylabel('Jumlah penyewaan sepeda')
    plt.grid(True)
    st.pyplot(plt)

with tab3:
    st.write("Penyewaan sepeda lebih banyak terjadi saat workingday atau holiday?")
    st.write("Berdasarkan visualisasi data di bawah, dapat disimpulkan bahwa day_status menentukan banyaknya penyewa sepeda. Penyewaan sepeda lebih banyak terjadi saat workingday")
    plt.figure(figsize=(8, 5))
    plt.bar(df3['day_status'], df3['cnt'], color=["#72BCD4", "#D3D3D3"])
    plt.title('Total Bike Rentals by Day Status')
    plt.xlabel('Day Status')
    plt.ylabel('Total Bike Rentals')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)

plt.cla()
with tab4:
    st.write("Pada jam berapa jumlah penyewaan sepeda tertinggi terjadi?")
    st.write("Berdasarkan visualisasi data di bawah dapat disimpulkan bahwa penyewaan sepeda tertinggi terjadi pada jam 17 untuk setiap musim")
    for season in df5['season'].unique():
        season_data = df4[df4['season'] == season]
        plt.plot(season_data['hr'], season_data['cnt'], label=season)

    plt.xlabel('Hour')
    plt.ylabel('Total Bike Rentals')
    plt.title('Total Bike Rentals by Hour for Each Season')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(0, 24))
    plt.show()

    st.pyplot(plt)

with tab5:
    st.subheader("Conclusion")
    st.write('''
- Analisis 1 : Berdasarkan hasil visualisasi pada tab "Hasil Analisis 1", dapat disimpulkan bahwa penyewaan sepeda paling banyak terjadi pada season Fall dan paling sedikit pada season springer
- Analisis 2 : Berdasarkan visualisasi data pada tab "Hasil Analisis 2" dapat disimpulkan penyewaan sepeda paling banyak terjadi pada 15 September 2012, yaitu 8714 sepeda. Berdasarkan visualisasi data pada tab "Hasil Analisis 2" dapat disimpulkan penyewaan sepeda paling sedikit terjadi pada 29 Oktober 2012, yaitu 22 sepeda
- Analisis 3 : Berdasarkan visualisasi data pada tab "Hasil Analisis 3", dapat disimpulkan bahwa day_status menentukan banyaknya penyewa sepeda. Penyewaan sepeda lebih banyak terjadi saat workingday"
- Analisis 4 : Berdasarkan visualisasi data pada tab "Hasil Analisis 4" dapat disimpulkan bahwa penyewaan sepeda tertinggi terjadi pada jam 17 untuk setiap musim"
'''
)