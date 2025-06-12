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

- **Python**, **Pandas**, **NumPy**, **TensorFlow**
- **Scikit-learn**, **Matplotlib**, **Seaborn**
- **TF-IDF**, **Cosine Similarity**, **Collaborative Filtering**

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
  - `cf/` - Model dengan format SavedModel
  - `tfjs_model/` - Model dengan format tfjs
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

```python
# Contoh CBF
get_recommendations("Danau Toba Parapat")

# Contoh CF
predict_rating_py("user123", "Danau Toba Parapat")
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
