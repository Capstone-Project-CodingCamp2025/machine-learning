# SIRESITA - Sistem Rekomendasi Wisata Sumatera Utara

**Proyek Capstone - Coding Camp 2025**  
**ID Tim:** CC25-CF119

## 📌 Ringkasan Proyek

SIRESITA adalah sistem rekomendasi wisata berbasis machine learning yang dirancang untuk membantu pengguna menemukan destinasi tersembunyi di Sumatera Utara, Indonesia. Proyek ini menggabungkan **Content-Based Filtering (CBF)** dan **Collaborative Filtering (CF)** untuk memberikan rekomendasi wisata yang personal dan relevan. Sistem ini dibangun secara modular yang mencakup ETL, model ML, dan integrasi layanan web.

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
  - `tfjs_model/`
  - `user_encoder.json`
  - `item_encoder.json`

---

## 🏗️ Struktur Proyek

```
.
├── etl_pipeline/
│   ├── extract.py
│   ├── load.py
│   ├── transform.py
│   ├── main.py
│   └── utils/
├── data/
│   ├── data_Wisata*.csv
│   ├── all_data.csv
│   ├── description.csv
├── model/
│   ├── CBF/
│   ├── CF/
├── notebook/
│   ├── Capstone_Model_CBF.ipynb
│   ├── Capstone_Model_CF.ipynb
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
- Dataset final: `transformed.csv`.

---

## 🚀 Contoh Inference

```python
# Contoh CBF
get_recommendations("Danau Toba Parapat")

# Contoh CF
predict_rating_py("user123", "Danau Toba Parapat")
```

---

## 💡 Fitur Utama

- Rekomendasi personalisasi untuk destinasi wisata.
- Sistem rekomendasi berdasarkan kemiripan konten dan interaksi pengguna.
- Visualisasi interaktif dan eksplorasi data.
- Model dan metadata dapat diekspor.

---

## 🛠️ Teknologi yang Digunakan

- **Python**, **Pandas**, **NumPy**, **TensorFlow**
- **Scikit-learn**, **Matplotlib**, **Seaborn**
- **TF-IDF**, **Cosine Similarity**, **Collaborative Filtering**
- **Vercel**, **ReactJS**, **TailwindCSS** (frontend tidak dibahas di sini)

---

## 📦 Instalasi

```bash
pip install -r requirements.txt
```

---

## 📍 Anggota Tim

- Sean Andrianto (ML)
- Bimo Birra (ML)
- Ferri Krisdiantoro (ML)
- Dzakkiyansyah (FE/BE)
- Sanu Ahadi W (FE/BE)
- Diah Putri Kartikasari (FE/BE)

---

## 📄 Lisensi

Lisensi MIT.
