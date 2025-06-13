# SIRESITA - Sistem Rekomendasi Wisata Sumatera Utara bagian Machine Learning

**Proyek Capstone - Coding Camp 2025**  
**ID Tim:** CC25-CF119

## 📌 Ringkasan Proyek bagian Machine Learning

**SIRESITA** bagian machine learning adalah proyek Capstone yang dikembangkan untuk membangun sistem rekomendasi tempat wisata di Sumatera Utara menggunakan dua pendekatan utama Machine Learning: **Content-Based Filtering (CBF)** dan **Collaborative Filtering (CF)**. Sistem ini tidak menggunakan model dari API eksternal atau pretrained model, melainkan dibangun sepenuhnya dari awal menggunakan TensorFlow dan scikit-learn.

---

## 💡 Fitur Utama

- Rekomendasi personalisasi untuk destinasi wisata.
- Sistem rekomendasi berdasarkan kemiripan konten dan interaksi pengguna.
- Visualisasi interaktif dan eksplorasi data.
- Model dan metadata dapat diekspor.

---

## 🛠️ Teknologi yang Digunakan

- Framework : **Python**, **TensorFlow**
- Manipulasi Data : **Pandas**, **NumPy**
- Visualisasi : **Matplotlib**, **Seaborn**
- Ekstraksi Fitur : **TF-IDF**, **Cosine Similarity**
- Pembuatan Model : **Scikit-learn**, **Keras**

---

## 🧠 Model Machine Learning

### ✅ Content-Based Filtering (CBF)
- Menggunakan TF-IDF untuk mengekstrak fitur dari nama tempat, deskripsi, dan kategori.
- Menghitung kemiripan menggunakan Cosine Similarity.
- Skor hybrid berdasarkan popularitas dan kategori.
- Output:
  - `cosine_similarity_matrix.npy`
  - `tourism_recommendation_model.json`
  - `tfidf_parameters.json`

### ✅ Collaborative Filtering (CF)
- Dibangun dengan TensorFlow menggunakan embedding untuk user dan item.
- Dilatih menggunakan data rating.
- Disimpan dalam format SavedModel TensorFlow dan dikonversi ke TF.js.
- Output:
  - `cf/` # Model dengan format SavedModel
  - `tfjs_model/` # Model dengan format tfjs
  - `encoders.json`

---

## 🏗️ Struktur Proyek

```
├── dataset/CF.csv
├── etl_pipeline/
│   ├── utils/
│   │   ├── extract.py
│   │   ├── load.py
│   │   └── transform.py
│   ├── data/*.csv
│   ├── main.py
│   ├── requirements.txt
│   └── transformed.csv
├── model/
│   ├── CBF/
│   │   ├── cosine_similarity_matrix.npy
│   │   ├── tourism_recommendation_model.json
│   │   ├── tfidf_parameters.json
│   │   └── requirements.txt
│   └── CF/
│   │   ├── cf/ - SavedModel
│   │   ├── tfjs_model/ - TFJS
│   │   ├── requirements.txt
│   └── └── encoders.json
├── notebook/
│   ├── Capstone_Model_CBF.ipynb
│   ├── Capstone_Model_CBF.py
│   ├── Capstone_Model_CF.ipynb
│   └── Capstone_Model_CF.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline ETL

Terdapat di folder `etl_pipeline/`:
- `extract.py`: Scraping data wisata dari Google Maps via SerpAPI.
- `transform.py`: Membersihkan dan menggabungkan data gambar dan deskripsi.
- `load.py`: Memasukkan data ke basis data.
- `main.py`: Menjalankan pipeline ETL secara keseluruhan.

---

## 📊 Data

- File CSV berdasarkan kategori: wisata alam, budaya, kuliner, belanja, edukasi.
- Enrichment deskripsi dan gambar.
- Dataset :
```
├── dataset/CF.csv - Dataset Collaborative Filtering
├── etl_pipeline/
└── └── transformed.csv - Dataset Content Base Filtering
```
---

## 🧠 Desain Model

### 📌 Content-Based Filtering (CBF)
- **Input**: `nama_tempat`, `deskripsi`, `kategori` → dikombinasikan jadi satu fitur teks.
- **Preprocessing**: 
  - Text cleaning
  - TF-IDF Vectorization
  - Cosine Similarity computation
- **Output**:
  - Matrix kemiripan antar tempat wisata
  - JSON metadata & parameter model
- **Model Inference**:
  ```python
  from capstone_model_cbf import get_recommendations
  recs = get_recommendations("Danau Toba Parapat", top_n=5)
  print(recs)
  ```

### 📌 Collaborative Filtering (CF)
- **Input**: user_id, item_id, rating
- **Preprocessing**: Label encoding → matrix factorization (Neural Embedding)
- **Model**: TensorFlow Embedding Layer + Dot Product + Bias
- **Output**:
  - Model TensorFlow SavedModel + TFJS export
  - user_encoder.json & item_encoder.json
- **Model Inference**:
  ```python
  from capstone_model_cf import predict_rating_py
  rating = predict_rating_py("user123", "place456")
  print(rating)
  ```

---

## 🚀 Contoh Inference

### Content Base Filtering
```python
def interactive_recommendation():
    """Interactive recommendation function"""
    print("\n🔍 Available Tourism Places:")
    for i, place in enumerate(df_clean['nama_tempat'].head(10), 1):
        print(f"{i}. {place}")

    print(f"\nTotal places available: {len(df_clean)}")

    # Example recommendations
    example_places = ['Danau Toba Parapat', 'Bukit Indah Simarjarunjung', 'Air Terjun Sikulikap']

    for place in example_places:
        if place in df_clean['nama_tempat'].values:
            print(f"\n🏞️ Recommendations for '{place}':")
            recs = get_recommendations(place, top_n=3)
            if recs is not None:
                for idx, rec in recs.iterrows():
                    print(f"  • {rec['nama_tempat']} ({rec['kategori']}) - Rating: {rec['rating']:.1f}")

interactive_recommendation()

print(f"\n🎉 Tourism Recommendation System Complete!")
print(f"📊 Dataset processed: {len(df_clean)} tourism places")
print(f"🏷️ Categories available: {df_clean['kategori'].nunique()}")
print(f"⭐ Average rating: {df_clean['rating'].mean():.2f}")
print(f"🔤 TF-IDF features: {tfidf_matrix.shape[1]}")
```

### Collaborative Filtering
```python
def get_tourism_recommendations(user_id, top_k=10):
    # Ambil places yang sudah dikunjungi user
    places_visited_by_user = df[df['user_id'] == user_id]

    # Ambil places yang belum dikunjungi
    places_not_visited = df[~df['place_id'].isin(places_visited_by_user['place_id'].values)]['place_id'].unique()

    # Filter places yang ada di encoding
    places_not_visited = list(
        set(places_not_visited).intersection(set(place_to_place_encoded.keys()))
    )

    if len(places_not_visited) == 0:
        print(f"User {user_id} sudah mengunjungi semua tempat wisata dalam dataset")
        return

    # Encode places yang belum dikunjungi
    places_not_visited_encoded = [[place_to_place_encoded.get(x)] for x in places_not_visited]

    # Encode user
    user_encoder = user_to_user_encoded.get(user_id)
    if user_encoder is None:
        print(f"User {user_id} tidak ditemukan dalam dataset")
        return

    # Buat array untuk prediksi
    user_place_array = np.hstack(
        ([[user_encoder]] * len(places_not_visited_encoded), places_not_visited_encoded)
    )

    # Prediksi rating
    ratings = model.predict(user_place_array).flatten()

    # Ambil top-k rekomendasi
    top_ratings_indices = ratings.argsort()[-top_k:][::-1]
    recommended_place_ids = [
        place_encoded_to_place.get(places_not_visited_encoded[x][0]) for x in top_ratings_indices
    ]

    # Tampilkan hasil
    print(f'Menampilkan rekomendasi untuk User: {user_id}')
    print('=' * 50)

    # Tampilkan tempat yang sudah dikunjungi dengan rating tinggi
    print('Tempat wisata dengan rating tinggi dari user:')
    print('-' * 40)

    top_places_user = (
        places_visited_by_user.sort_values(by='rating', ascending=False)
        .head(5)
        .place_id.values
    )

    for place_id in top_places_user:
        # Cari info tempat wisata (jika ada di tourism_df)
        place_info = tourism_df[tourism_df['id'] == place_id]
        if not place_info.empty:
            place_name = place_info.iloc[0]['nama_tempat']
            place_category = place_info.iloc[0]['kategori']
            user_rating = places_visited_by_user[places_visited_by_user['place_id'] == place_id]['rating'].iloc[0]
            print(f"- {place_name} ({place_category}) - Rating user: {user_rating}")
        else:
            user_rating = places_visited_by_user[places_visited_by_user['place_id'] == place_id]['rating'].iloc[0]
            print(f"- Place ID {place_id} - Rating user: {user_rating}")

    print('-' * 40)
    print(f'Top {top_k} Rekomendasi Tempat Wisata:')
    print('-' * 40)

    for i, place_id in enumerate(recommended_place_ids, 1):
        # Cari info tempat wisata (jika ada di tourism_df)
        place_info = tourism_df[tourism_df['id'] == place_id]
        if not place_info.empty:
            place_name = place_info.iloc[0]['nama_tempat']
            place_category = place_info.iloc[0]['kategori']
            place_rating = place_info.iloc[0]['rating']
            predicted_rating = ratings[top_ratings_indices[i-1]]
            print(f"{i}. {place_name} ({place_category})")
            print(f"   Rating rata-rata: {place_rating}, Prediksi rating user: {predicted_rating:.3f}")
        else:
            predicted_rating = ratings[top_ratings_indices[i-1]]
            print(f"{i}. Place ID {place_id} - Prediksi rating: {predicted_rating:.3f}")

sample_user = df['user_id'].sample(1).iloc[0]
get_tourism_recommendations(sample_user, top_k=5)

get_tourism_recommendations(39, top_k=5)
```

---

## ⚙️ Instalasi & Setup

### Clone & Virtual Env
```bash
git clone <repo-url>
cd <project-dir>
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate   # (Windows)
```

### Instalasi Dependensi
```bash
pip install -r requirements.txt
pip install -r model/CBF/requirements.txt
pip install -r model/CF/requirements.txt
```

---

## 📌 Catatan Kepatuhan Capstone

✅ Tidak menggunakan model dari TensorFlow Hub, HuggingFace, ChatGPT API, atau AutoML  
✅ Model dibangun dari awal  
✅ Inference diimplementasikan dengan kode Python sederhana  
✅ Model CF diekspor ke TensorFlow.js untuk integrasi front-end  

---

## 📍 Anggota Tim Machine Learning

- Sean Andrianto | Leader
- Ferri Krisdiantoro | Model Building dan Model Deployment
- Bimo Birra | Data Scarping dan Data Cleaning

---

## 📄 Lisensi

Proyek ini dibuat untuk kebutuhan Capstone **Coding Camp 2025**. Lisensi: MIT.  
