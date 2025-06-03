from utils.extract import scrape_web
from utils.transform import transform_data
from utils.load import to_db

def main():
    # Scrape Web
    wisata_alam = scrape_web('Wisata Alam Sumatra Utara')
    wisata_kuliner = scrape_web('Wisata Kuliner Sumatra Utara', max_data=50)
    wisata_budaya_sejarah = scrape_web('Wisata Budaya dan Sejarah Sumatra Utara', max_data=40)
    wisata_edukasi = scrape_web('Wisata Edukasi Sumatra Utara', max_data=30)
    wisata_belanja = scrape_web('Wisata Belanja Sumatra Utara', max_data=30)
    
    # Mengabungkan Data
    wisata_alam = pd.read_csv('data/data_Wisata Alam Sumatra Utara.csv')
    wisata_belanja = pd.read_csv('data/data_Wisata Belanja Sumatra Utara.csv')
    wisata_budaya_sejarah = pd.read_csv('data/data_Wisata Budaya dan Sejarah Sumatra Utara.csv')
    wisata_edukasi = pd.read_csv('data/data_Wisata Edukasi Sumatra Utara.csv')
    wisata_kuliner = pd.read_csv('data/data_Wisata Kuliner Sumatra Utara.csv')

    all_data = pd.concat([wisata_alam, wisata_belanja, wisata_budaya_sejarah, wisata_edukasi, wisata_kuliner], ignore_index=True)

    all_data.to_csv('all_data.csv', index=False)
    
    # Transform Data
    semua_data = pd.read_csv('all_data.csv')
    
    transform_data(semua_data)
    
    # Load Data ke dalam Database
    transformed = pd.read_csv('transformed.csv')
    
    to_db(transformed, db_url)