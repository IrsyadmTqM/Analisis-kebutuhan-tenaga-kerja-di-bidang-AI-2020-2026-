# Analisis Peluang Karier AI 2020-2026: Menguak Potensi Gaji Remote Entry-Level di Sektor Startup

Analisis strategis mengenai dinamika pasar kerja Kecerdasan Buatan global, dengan fokus khusus pada peran *Remote*, *Entry-Level*, dan sektor *Startup*.

## Dataset
Data yang digunakan dalam analisis ini bersumber dari Kaggle:
[AI and Data Science Job Market Dataset 2020-2026](https://www.kaggle.com/datasets/shree0910/ai-and-data-science-job-market-dataset-20202026)

---

## Visualisasi Tren Gaji
![Tren Gaji AI di Startup](image.png)
*Grafik: Tren Kenaikan/Penurunan Gaji AI di Sektor Startup (Remote & Entry-Level)*

---

## Deskripsi Proyek
Proyek ini menyajikan analisis komprehensif mengenai dinamika pasar kerja di bidang **Kecerdasan Buatan (Artificial Intelligence)**. Fokus utama penelitian ini adalah pada peluang kerja jarak jauh (*remote*) bagi tenaga kerja tingkat pemula (*entry-level*). 

Dengan memanfaatkan dataset pasar kerja AI global, analisis ini bertujuan untuk memberikan wawasan mendalam mengenai:
* Tren kompensasi tahunan.
* Stabilitas peran pekerjaan tertentu.
* Pergeseran permintaan industri selama periode tujuh tahun (2020-2026).

---

## Wawasan Utama (Executive Summary)
Melalui serangkaian visualisasi data menggunakan Python, proyek ini berhasil mengidentifikasi beberapa tren krusial:

* **Dominasi Peran Inti AI:** Posisi *AI Engineer* dan *Machine Learning Engineer* secara konsisten menempati hierarki kompensasi tertinggi di sektor Startup, dengan rata-rata gaji tahunan melampaui ambang batas **$110.000**.
* **Volatilitas Sektor Startup:** Berbeda dengan perusahaan multinasional (MNC), sektor Startup menunjukkan volatilitas gaji yang lebih tinggi. Hal ini mencerminkan respons cepat industri terhadap inovasi teknologi dan kondisi pendanaan ventura.
* **Kebangkitan Data Engineering:** Analisis tren menunjukkan pemulihan dan pertumbuhan konsisten pada peran *Data Engineer* sejak tahun 2022. Ini mengindikasikan peningkatan kesadaran industri akan pentingnya infrastruktur data yang matang sebelum implementasi model AI.
* **Stabilitas Karier:** Peran *AI Engineer* teridentifikasi sebagai posisi yang paling stabil secara finansial, menunjukkan resistensi yang kuat terhadap fluktuasi pasar dibandingkan peran teknis lainnya di level pemula.

---

## Metodologi Pengolahan Data
Analisis ini dilakukan melalui tahapan sistematis sebagai berikut:

1.  **Ekstraksi Data:** Memuat dataset primer `AI_Job_Market_Dataset.csv` ke dalam *data frame*.
2.  **Pembersihan & Transformasi:** Melakukan filtrasi berlapis untuk menyaring data berdasarkan kriteria spesifik:
    * **Remote Type:** `Remote`
    * **Experience Level:** `Entry`
    * **Company Size:** `Startup`
3.  **Agregasi Statistik:** Menghitung rata-rata gaji tahunan per posisi pekerjaan menggunakan metode *grouping* berdasarkan tahun posting (`job_posting_year`).
4.  **Visualisasi Data:** Mengonstruksi grafik garis (*Time-Series Analysis*) menggunakan Matplotlib untuk memetakan lintasan pertumbuhan gaji secara akurat dan mudah dipahami.

---

## Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python
* **Library Analisis:** Pandas
* **Library Visualisasi:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebook

---
