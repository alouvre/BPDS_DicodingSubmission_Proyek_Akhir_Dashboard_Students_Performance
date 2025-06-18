# 🏢 Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

Proyek ini bertujuan untuk menyelesaikan permasalahan tingginya angka dropout di sebuah institusi pendidikan bernama Jaya Jaya Institut dengan pendekatan berbasis data. Solusi yang dikembangkan mencakup eksplorasi dan analisis data, visualisasi melalui dashboard interaktif menggunakan Metabase, serta pembangunan sistem prediksi dropout berbasis machine learning menggunakan Streamlit. Prototype sistem ini juga telah disiapkan untuk di-deploy melalui Streamlit Community Cloud agar dapat dijalankan di environment cloud dan diakses secara remote.

[Video presentasi klik disini](https://drive.google.com/drive/folders/1hfHebrK4XbpF6knjkn9j3K5LELnbHVux?usp=sharing)

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

## 📊 Persiapan Business Dashboarding dengan Metabase

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

```
🌐 http://localhost:3000/setup
```

Untuk mulai menggunakan dashboard Metabase dan melihat visualisasi data.

Anda bisa login ke dashboard Metabase menggunakan:

```
alifiamustika02@gmail.com
root@123
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

## 🧠 Machine Learning Modeling

Sebuah model klasifikasi dikembangkan untuk memprediksi apakah seorang mahasiswa memiliki kemungkinan untuk mengalami dropout dari institusi pendidikan Jaya Jaya Institut. Proses pemodelan difokuskan pada identifikasi pola-pola dalam data akademik, sosial, dan ekonomi yang dapat mengindikasikan risiko dropout. Dengan model ini, pihak akademik dapat mengambil langkah preventif secara proaktif untuk meningkatkan retensi mahasiswa.

### ✅ `Pendekatan yang Digunakan:`

- LazyClassifier (Baseline Model Selection)

  Digunakan untuk membandingkan berbagai algoritma klasifikasi secara cepat dan efisien. Dari hasil perbandingan, algoritma XGBClassifier dipilih karena menghasilkan akurasi tertinggi sebesar 0.90, menjadikannya kandidat utama untuk pelatihan lanjutan.

- XGBoost Classifier (Model Utama)

  Merupakan algoritma klasifikasi yang cepat dan efisien untuk data tabular. Digunakan sebagai model utama untuk memprediksi risiko dropout, baik sebelum maupun sesudah proses seleksi fitur, guna mengukur pengaruh penyederhanaan fitur terhadap performa model.

- Heatmap Korelasi dan Feature Importance

  Digunakan untuk mengidentifikasi fitur-fitur yang paling berpengaruh terhadap keputusan model. Fitur penting yang terdeteksi antara lain:

  ```
  MothersQualification, FathersQualification, MothersOccupation, FathersOccupation,
  CurricularUnits1stSemCredited, CurricularUnits1stSemEnrolled, CurricularUnits1stSemEvaluations, CurricularUnits1stSemApproved, CurricularUnits1stSemGrade, CurricularUnits2ndSemCredited,
  CurricularUnits2ndSemEnrolled, CurricularUnits2ndSemEvaluations,
  CurricularUnits2ndSemApproved, CurricularUnits2ndSemGrade
  ```

- Lingkungan Pengembangan: Jupyter Notebook

  Model dikembangkan dalam Jupyter Notebook menggunakan library Python seperti pandas untuk manipulasi data dan scikit-learn untuk preprocessing, pelatihan, dan evaluasi model.

- Evaluasi Model: Accuracy, Precision, Recall, F1-score, dan Confusion Matrix

  Metrik ini memberikan gambaran menyeluruh tentang performa model dalam memprediksi status mahasiswa (dropout atau graduate).

### 📉 `Kinerja Model:`

- Evaluasi Model XGBoost:

  - Accuracy = 0.90, Precision = 0.90, Recall = 0.90, F1 Score = 0.89
  - Confusion Matrix:

    ```python
    [[291, 64],
    [ 31, 522]]
    ```

- 📌 Interpretasi:

  Model menunjukkan performa yang kuat dan seimbang dalam mengklasifikasikan mahasiswa yang dropout maupun yang lulus (graduate).

  - Dari `322` mahasiswa yang benar-benar dropout, model berhasil mendeteksi 291 di antaranya (recall tinggi terhadap kelas dropout).
  - Sementara dari `586` mahasiswa yang lulus, model berhasil mengklasifikasikan 522 dengan benar.

  Hal ini menunjukkan bahwa model memiliki kemampuan deteksi yang baik terhadap kasus dropout, yang sangat penting untuk intervensi dini oleh pihak institusi.

<br>

## 🌐 Langkah-Langkah Menjalankan Sistem Machine Learning

Setelah proses pelatihan (training) model selesai, model disimpan dalam format `.joblib` menggunakan library `joblib`. Untuk menggunakan model tersebut dalam proses prediksi data mahasiswa baru, tersedia sebuah file bernama `app.py` yang dapat dijalankan menggunakan Streamlit.

1. Membuat dan Mengaktifkan Virtual Environment (venv)

   Agar proses pengembangan tetap stabil dan terisolasi dari sistem utama, disarankan untuk menggunakan virtual environment.

   `📦 Membuat virtual environment`

   ```bash
   python -m venv venv
   ```

   `▶️ Mengaktifkan environment`

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

2. Menginstal Library yang Dibutuhkan

   Setelah virtual environment aktif, jalankan perintah berikut untuk menginstal dependensi:

   ```bash
   pip install pandas scikit-learn joblib streamlit xgboost numpy
   ```

   Penjelasan:

   - `pandas`: Untuk membaca dan memproses data mahasiswa dalam format tabel.
   - `numpy`: Digunakan untuk manipulasi array dan struktur data numerik, termasuk dalam proses prediksi dan preprocessing.
   - `scikit-learn`: Library utama untuk machine learning (pelatihan dan prediksi).
   - `joblib`: Untuk memuat model yang telah disimpan sebelumnya.
   - `streamlit`: Untuk menjalankan aplikasi web prediksi secara interaktif.
   - `xgboost`: Digunakan untuk memuat dan menjalankan model XGBoost (model utama yang digunakan).

3. Menjalankan Aplikasi Prediksi

   Jalankan aplikasi menggunakan perintah berikut:

   ```bash
   streamlit run app.py
   ```

   Penjelasan:

   - `app.py` adalah skrip Python yang berisi logika untuk:
     - Membaca data mahasiswa baru.
     - Memuat model prediksi yang sudah disimpan.
     - Melakukan prediksi apakah mahasiswa tersebut berisiko dropout atau tidak.
     - Menampilkan atau menyimpan hasil prediksi.

4. Alternatif: Jalankan Online

   Jika Anda tidak ingin menjalankan secara lokal, Anda dapat mengakses aplikasi yang sudah dideploy di Streamlit Community Cloud melalui tautan berikut:

   ```
   🔗 https://dashboardstudentsperformance.streamlit.app/
   ```
