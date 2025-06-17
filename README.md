# 🏢 Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

Proyek ini bertujuan untuk menyelesaikan permasalahan tingginya angka dropout di sebuah institusi pendidikan bernama Jaya Jaya Institut dengan pendekatan berbasis data. Solusi yang dikembangkan mencakup eksplorasi dan analisis data, visualisasi melalui dashboard interaktif menggunakan Metabase, serta pembangunan sistem prediksi dropout berbasis machine learning menggunakan Streamlit. Prototype sistem ini juga telah disiapkan untuk di-deploy melalui Streamlit Community Cloud agar dapat dijalankan di environment cloud dan diakses secara remote.


<br>

## 📁 Struktur Direktori

```
submission
├───data
     ├───data_student.csv
     ├───data_student_cleaned.csv
     ├───data_student_dashboard.csv
     ├───data_student_final.csv
     ├───data_student_preprocessed.csv
├───images
     ├───alouvre-dashboard
├───models
     ├───model_xgboost.pkl
     ├───model_xgboost.joblib
     ├───scaler.pkl
     ├───label_encoders.pkl
├───metabase.db
     ├───metabase.db.mv
├───notebook.ipynb
├───app.py
├───README.md
├───documentation.md
├───alouvre-video
└───requirements.txt
```

📝 Penjelasan Berkas Utama:

- `models/` - Folder berisi file model (.pkl) dan objek pendukung seperti scaler dan label encoder.
- `data/` - Berisi data mentah hingga data siap pakai untuk modeling dan dashboarding.
- `metabase/` -
- `README.md` - Ini file yang berisi gambaran umum tentang proyek, misalnya tujuan, cara pakai, atau ringkasan proyek.
- `documentation.md` - Ini dokumen yang menjelaskan detail tentang proyek, bisa lebih lengkap dari README, biasanya cara kerja, spesifikasi teknis, dan lain-lain.
- `models/model_xgboost.pkl` - Ini file model machine learning yang sudah dilatih menggunakan algoritma Perceptron.
- `models/scaler.pkl` - File yang berisi scaler, biasanya digunakan untuk preprocessing data agar fitur-fiturnya berada di skala yang sama sebelum dimasukkan ke model.
- `app.py` - Script/program untuk melakukan prediksi menggunakan model yang sudah dilatih.
- `data/data_student_dashboard.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk pembuatan dashboard.
- `data/data_student_final.csv` - Dataset yang sudah diproses atau dibersihkan, siap dipakai untuk training model.
- `data/data_student.csv` - Dataset asli sebelum dibersihkan atau diproses.
- `notebook.ipynb` - Jupyter Notebook berisi proses pemodelan, analisis data, training model, dll.
- `metabase/metabase.db.mv.db` - File database dari Metabase yang berisi data, pertanyaan yang sudah disimpan, dan dashboard visualisasi.
- `requirements.txt` - File yang mencantumkan semua dependensi Python yang dibutuhkan untuk menjalankan proyek.

<br>

## 📊 Persiapan Business dashboarding dengan Metabase

Dataset yang digunakan berasal dari Universitas fiktif Jaya Jaya Institut, yang tersedia di repositori berikut:

- 🔗 [Dataset Jaya Jaya Institut](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv).

### Install requirements

Pastikan semua library yang dibutuhkan telah terinstall:

```python
pip install -r requirements.txt
```

### Setup metabase

Untuk menjalankan Metabase secara lokal menggunakan Docker:

```python
docker run -d -p 3000:3000 --name metabase \
  -v "$(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db" \
  metabase/metabase
```

Setelah container berjalan, buka browser dan akses:

🌐 http://localhost:3000/setup

Untuk mulai menggunakan dashboard Metabase dan melihat visualisasi data.

Anda bisa login ke dashboard Metabase menggunakan:
```
root@mail.com
root123
```

### Setup supabase

- Buat akun dan login https://supabase.com/dashboard/sign-in.
- Buat new project
- Copy URI pada database setting
- Kirim dataset menggunakan sqlalchemy

  ```python
  from sqlalchemy import create_engine

  URL = "DATABASE_URL"

  engine = create_engine(URL)
  df.to_sql('dataset', engine)
  ```

<br>


