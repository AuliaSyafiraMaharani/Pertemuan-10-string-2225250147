# Latihan 6: Pencarian Kata

teks = "Python untuk data. Python untuk pendidikan."
teks_lower = teks.lower()
kata = "python"

print("Apakah kata terdapat dalam teks? :", kata in teks_lower)
print("Jumlah kemunculan kata           :", teks_lower.count(kata))
print("Indeks posisi pertama ditemukan   :", teks_lower.find(kata))