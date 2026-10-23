# Latihan 4: Membersihkan Teks dari Spasi Ganda

teks = "  belajar   python   untuk   pendidikan  "

# Membersihkan spasi di awal dan akhir
teks = teks.strip()

# Mengurangi spasi ganda di tengah menjadi spasi tunggal
while "  " in teks:
    teks = teks.replace("  ", " ")

print("Teks bersih        :", teks)
print("Hasil capitalize() :", teks.capitalize())