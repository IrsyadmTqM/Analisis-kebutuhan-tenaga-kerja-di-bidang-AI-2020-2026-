# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# 1. Membaca data dari file CSV
# Ubah nama file di bawah ini jika nama file CSV-mu berbeda
df = pd.read_csv("AI_Job_Market_Dataset.csv")

# 2. MENGINTIP DATA: Melihat 5 baris pertama dan daftar nama kolom
print("Daftar Kolom dalam Dataset:")
print(df.columns) # Ini sangat penting agar kita tahu nama kolomnya!
print(df.head())

# %%
# 1. Membaca data (Pandas sudah kita lakukan di atas, jadi kita lanjut ke langkah berikutnya)


# 2. Mengolah Data: Mengelompokkan berdasarkan 'job_title' dan MENJUMLAHKAN 'job_openings'
# Kita gunakan sum() karena kita ingin menjumlahkan total orang yang dicari, bukan sekadar menghitung jumlah iklannya
total_lowongan = df.groupby('job_title')['job_openings'].sum()

# Mengambil 10 pekerjaan dengan lowongan terbanyak, lalu diurutkan dari yang terkecil agar grafiknya rapi
top_10_lowongan = total_lowongan.nlargest(10).sort_values(ascending=True)

print("Top 10 Posisi dengan Lowongan Terbanyak:")
print(top_10_lowongan)

# %%
# 3. Membuat Visualisasi: Bar Chart Horizontal
plt.figure(figsize=(10, 6))

# Membuat diagram batang mendatar
plt.barh(top_10_lowongan.index, top_10_lowongan.values, color='mediumseagreen')

# Menambahkan judul dan label
plt.title('Top 10 Pekerjaan AI dengan Total Lowongan Terbanyak', fontsize=14, fontweight='bold')
plt.xlabel('Total Kebutuhan Karyawan (Job Openings)', fontsize=12)
plt.ylabel('Posisi Pekerjaan (Job Title)', fontsize=12)

# Menambahkan grid vertikal agar angka lebih mudah dibaca
plt.grid(axis='x', linestyle='--', alpha=0.6)

# %%
# 4. Menampilkan plot
plt.show()

# %%