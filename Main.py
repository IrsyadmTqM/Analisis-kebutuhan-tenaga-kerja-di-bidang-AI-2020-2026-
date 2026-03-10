# %%
import pandas as pd
import matplotlib.pyplot as plt

# 1. Membaca data
df = pd.read_csv("AI_Job_Market_Dataset.csv")

# 2. FILTERING DATA (Menambahkan syarat 'Startup')
# Kita gunakan tanda '&' untuk menggabungkan 3 syarat sekaligus
df_startup_remote = df[
    (df['company_size'] == 'Startup') & 
    (df['remote_type'] == 'Remote') & 
    (df['experience_level'] == 'Entry')
]

# 3. MENGOLAH DATA TAHUNAN
# Mengelompokkan berdasarkan Tahun dan Judul Pekerjaan
tren_gaji_startup = df_startup_remote.groupby(['job_posting_year', 'job_title'])['salary'].mean().unstack()

print("Tabel Rata-rata Gaji per Tahun (Startup - Remote - Entry):")
print(tren_gaji_startup)

# %%
# 4. MEMBUAT VISUALISASI LINE CHART
plt.figure(figsize=(12, 7))

# Menggunakan warna yang lebih cerah (vibrant) ala startup
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FFB833', '#33FFF3']

# Membuat garis untuk setiap posisi pekerjaan
for i, posisi in enumerate(tren_gaji_startup.columns):
    plt.plot(tren_gaji_startup.index, 
             tren_gaji_startup[posisi], 
             marker='o', 
             label=posisi, 
             linewidth=3, 
             color=colors[i % len(colors)])

# Menambahkan judul dan label yang lebih spesifik
plt.title('Tren Gaji AI di STARTUP (Remote & Entry-Level)', fontsize=16, fontweight='bold')
plt.xlabel('Tahun Posting', fontsize=12)
plt.ylabel('Rata-rata Gaji (USD)', fontsize=12)

# Estetika Grafik
plt.xticks(tren_gaji_startup.index)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Posisi Pekerjaan", bbox_to_anchor=(1.05, 1), loc='upper left')

# %%
# 5. Menampilkan plot
plt.tight_layout()
plt.show()

# %%