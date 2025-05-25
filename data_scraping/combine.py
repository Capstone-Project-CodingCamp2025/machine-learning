import pandas as pd

# Menggabungkan semua Dataset menjadi satu

wisata_alam = pd.read_csv('data/data_Wisata Alam Sumatra Utara.csv')
wisata_belanja = pd.read_csv('data/data_Wisata Belanja Sumatra Utara.csv')
wisata_budaya_sejarah = pd.read_csv('data/data_Wisata Budaya dan Sejarah Sumatra Utara.csv')
wisata_edukasi = pd.read_csv('data/data_Wisata Edukasi Sumatra Utara.csv')
wisata_kuliner = pd.read_csv('data/data_Wisata Kuliner Sumatra Utara.csv')

all_data = pd.concat([wisata_alam, wisata_belanja, wisata_budaya_sejarah, wisata_edukasi, wisata_kuliner], ignore_index=True)
all_data.drop(columns=['Unnamed: 0'], inplace=True)

all_data.to_csv('all_data.csv')