def normalisasi_nama(nama: str) -> str:
    """
    Membersihkan spasi berlebih pada awal, akhir, dan antar kata,
    lalu mengembalikan nama dalam format Title Case.
    """
    # .split() tanpa argumen memisahkan string berdasarkan whitespace apa pun dan menghapus spasi berlebih
    kata = nama.strip().split()
    return " ".join(kata).title()


def buat_inisial(nama: str) -> str:
    """
    Menghasilkan inisial nama dari huruf awal setiap kata.
    """
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    return "".join(k[0] for k in kata).upper()


def normalisasi_kode(kode: str) -> str:
    """
    Membersihkan kode kelas, mengubahnya ke huruf besar,
    dan menggabungkan kata dengan tanda hubung (-).
    """
    kata = kode.strip().upper().split()
    return "-".join(kata)


def main():
    print("=== PROGRAM NORMALISASI DATA MAHASISWA ===")
    
    # Input dari pengguna
    nama_input = input("Nama       : ")
    kode_input = input("Kode kelas : ")
    
    # Proses normalisasi
    nama_bersih = normalisasi_nama(nama_input)
    kode_bersih = normalisasi_kode(kode_input)
    inisial = buat_inisial(nama_input)
    jumlah_kata = len(nama_bersih.split())
    
    # Output hasil
    print("\n=== HASIL NORMALISASI ===")
    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")


if __name__ == "__main__":
    main()