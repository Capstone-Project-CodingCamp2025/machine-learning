import os
import serpapi
import pandas as pd
import time
from dotenv import load_dotenv
load_dotenv()

# Mengambil Kunci API dari .env
api_key = os.getenv('API_KEY')

# Inisialisasi api SerpAPI
client = serpapi.Client(api_key=api_key)


def scrape_web(query, max_data=120, ll="@1.8335539,97.4222773,8z", start=0):
    '''
    Fungsi untuk melakukan scraping data dari Google Maps menggunakan SerpAPI.

    Args:
        query (str): Kueri pencarian yang akan digunakan (misalnya, "Wisata Alam Sumatra Utara").
        max_data (int, optional): Jumlah maksimum data tempat yang ingin dikumpulkan. Defaultnya 120.
        ll (str, optional): Parameter lintang, bujur, dan zoom untuk Google Maps. 
                           Defaultnya adalah koordinat untuk Sumatra Utara.
        start (int, optional): Indeks awal untuk hasil pencarian (untuk paginasi). Defaultnya 0.

    Returns:
        None: Fungsi ini menyimpan hasilnya langsung ke file CSV.
    '''
    data = []
    collected_place_ids = set()
    
    # Loop akan terus berjalan selama jumlah data yang terkumpul kurang dari max_data
    while len(data) < max_data:
        
    # Melakukan pencarian menggunakan SerpAPI
        results = client.search({
            'engine': 'google_maps', # Menentukan mesin pencari Google Maps
            'type': 'search', # Menentukan tipe pencarian
            'q': query, # Kueri pencarian
            'hl': 'id', # Mengatur bahasa hasil pencarian ke Bahasa Indonesia   
            'gl': 'id', # Mengatur negara pencarian ke Indonesia
            'start': start, # Indeks awal untuk hasil (paginasi)
            'll': ll, # Koordinat geografis dan zoom
        })

        places = results['local_results']
        
        # Iterasi melalui setiap tempat yang ditemukan
        for place in places:
            place_id = place.get('place_id') # Mendapatkan ID unik tempat
            if place_id and place_id not in collected_place_ids:
                # Membuat dictionary untuk menyimpan detail satu tempat
                all_data = {
                    'nama_tempat': place.get('title'),
                    'rating': place.get('rating'),
                    'jumlah_ulasan': place.get('reviews'),
                    'alamat': place.get('address'),
                    'link' : f"https://www.google.com/maps/place/?q=place_id:{place.get('place_id')}",
                    'thumbnail': place.get('thumbnail'),
                }
            
                data.append(all_data)

        start += len(places)
        time.sleep(5)

    # Menentukan nama kategori dari query dan menambahkan kolom kategori
    kategori = query.replace('Sumatra Utara', '').strip()

    df = pd.DataFrame(data)

    df.to_csv(f'data_{kategori}.csv')

    print(df)
    print(len(df))
    print('Data berhasil dijadikan csv')