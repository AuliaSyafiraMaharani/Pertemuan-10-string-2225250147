# Pertemuan 10 String dan Pengolahan Teks

Nama: Aulia Syafira Maharani 
NIM: 2225250147 
Kelas: 3A

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan

python3 tugas/normalisasi_data_mahasiswa.py

## Struktur Fungsi

* `normalisasi_nama(nama)` : Membersihkan spasi di awal/akhir dan mengubah format nama menjadi title case.
* `buat_inisial(nama)` : Membentuk inisial dari huruf awal setiap kata pada nama mahasiswa.
* `normalisasi_kode(kode)` : Mengubah kode kelas menjadi huruf kapital dan mengganti spasi dengan tanda hubung.

## Hasil Pengujian

| Fungsi | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| `normalisasi_nama` | `"  aan hendrayana  "` | `"Aan Hendrayana"` | `"Aan Hendrayana"` | Lulus |
| `buat_inisial` | `"Aan Hendrayana"` | `"AH"` | `"AH"` | Lulus |
| `normalisasi_kode` | `"pmat a 2026"` | `"PMAT-A-2026"` | `"PMAT-A-2026"` | Lulus |

## Refleksi

Pengolahan string sangat sensitif terhadap spasi berlebih dan perbedaan huruf besar/kecil. Penggunaan method gabungan seperti `.strip()`, `.split()`, dan `.join()` terbukti sangat efektif untuk merapikan data teks yang tidak konsisten sebelum diproses lebih lanjut.