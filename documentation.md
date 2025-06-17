# 🏢 Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

### Permasalahan Bisnis

### Cakupan Proyek

<br>

## Persiapan

Dataset yang digunakan berasal dari Universitas fiktif Jaya Jaya Institut, yang tersedia di repositori berikut:

- 🔗 [Dataset Jaya Jaya Institut](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv).

### Install requirements

Pastikan semua library yang dibutuhkan telah terinstall:

```python
pip install -r requirements.txt
```

<br>

## Business Dashboard

![Dashboard](images/alouvre-dashboard.png)

Dashboard ini dibangun menggunakan Metabase dan dirancang untuk menganalisis performa akademik dan risiko dropout mahasiswa di Jaya Jaya Institut. Dashboard ini membantu pihak institusi, seperti dosen wali dan manajer akademik, dalam mengidentifikasi mahasiswa yang berpotensi mengalami dropout serta memahami faktor-faktor yang memengaruhi kelulusan.


### Metrik Utama

| **Visualisasi**           | **Tujuan Analisis**                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Total Dropout Rate**    | Menunjukkan persentase keseluruhan mahasiswa yang mengalami dropout dari total populasi mahasiswa. |
| **Total Students**        | Jumlah total mahasiswa yang tercakup dalam data.                                                   |
| **Average Grade 1st Sem** | Menyajikan rata-rata nilai mahasiswa pada semester pertama.                                        |
| **Average Grade 2nd Sem** | Menunjukkan rata-rata nilai semester kedua, sebagai indikator progres akademik lanjutan.           |
| **Avg Age at Enrollment** | Menampilkan rata-rata usia mahasiswa saat pertama kali mendaftar.                                  |

### Visualisasi Berdasarkan Demografi dan Status

| **Visualisasi**         | **Tujuan Analisis**                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| **Distribution Status** | Menampilkan proporsi mahasiswa dengan status *Graduate*, *Dropout*, dan *Enrolled*.                     |
| **Gender by Dropout Status**    | Menganalisis distribusi status kelulusan berdasarkan jenis kelamin (Male vs Female).                    |
| **Course by Dropout Status**    | Menunjukkan jumlah mahasiswa per program studi berdasarkan status akhir mereka (lulus, dropout, aktif). |


### Faktor Sosial dan Ekonomi

| **Visualisasi**                          | **Tujuan Analisis**                                                                     |
| ---------------------------------------- | --------------------------------------------------------------------------------------- |
| **Scholarship Holder by Dropout Status** | Menganalisis hubungan antara kepemilikan beasiswa dengan risiko dropout mahasiswa.      |
| **Tuition Payment by Dropout Status**    | Menilai pengaruh keterlambatan atau kelancaran pembayaran SPP terhadap tingkat dropout. |


###  Performa Akademik Mahasiswa

| **Visualisasi**                        | **Tujuan Analisis**                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Total Passed Subjects (1st and 2nd Sem) by Dropout Status** | Menunjukkan seberapa banyak mata kuliah yang diselesaikan mahasiswa pada semester 1 dan 2 berdasarkan status. |
|                                        | Semakin sedikit mata kuliah yang diselesaikan, semakin besar kemungkinan mahasiswa mengalami *dropout*.       |

