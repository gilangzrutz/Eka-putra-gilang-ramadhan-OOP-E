# class>motor
# object> surat2, kondisi_mesin, model, harga, CC, warna
# nama : Muh Aril Mulyadi (24241164)

class SepedaMotor:
    def __init__(self, surat2, kondisi_mesin, merk, model, harga, cc, warna):
        # Instance variables
        self.surat2 = surat2
        self.kondisi_mesin = kondisi_mesin
        self.merk = merk
        self.model = model
        self.harga = harga
        self.cc = cc
        self.warna = warna

    def tampilkan_info(self):
        print("=== Informasi Sepeda Motor ===")
        print(f"Merk           : {self.merk}")
        print(f"Model          : {self.model}")
        print(f"Warna          : {self.warna}")
        print(f"Kapasitas Mesin: {self.cc} cc")
        print(f"Harga          : Rp{self.harga:,}")
        print(f"Kondisi Mesin  : {self.kondisi_mesin}")
        print(f"Surat-surat    : {self.surat2}")
        print()

# Membuat dua objek dengan instance variable berbeda
motor1 = SepedaMotor("Lengkap (STNK & BPKB)", "Baik", "Honda", "Beat", 18000000, 110, "Hitam")
motor2 = SepedaMotor("Lengkap (STNK & BPKB)", "Sangat Baik", "Honda", "Vario", 19000000, 110, "Abu")

# Memanggil method yang menggunakan instance variable
motor1.tampilkan_info()
motor2.tampilkan_info()