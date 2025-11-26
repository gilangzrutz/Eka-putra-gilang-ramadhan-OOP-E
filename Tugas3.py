class Data:
    def __init__(self, nama, usia, matakuliah, jurusan):
        self.nama = nama
        self.usia = usia
        self.matakuliah = matakuliah
        self.jurusan = jurusan
        
    def infoDosen(self):
        return (f"{self.nama} sedang mengajar matakuliah {self.matakuliah}")
        
    def infoMahasiswa(self):
        return (f"{self.nama} sedang belajar di jurusan {self.jurusan}")
    

class Dosen(Data):
    def __init__(self, nidn):
        self.nidn = nidn
        
        
class Mahasiswa(Data):
    def __init__(self, nim):
        self.nim = nim
        
        
dosen1 = Dosen("123456")
dosen1.nama = "Edy"
dosen1.matakuliah = "Pemrograman Berorientasi Objek"
dosen1.usia = 28
print(dosen1.infoDosen())

mahasiswa1 = Mahasiswa("24241166")
mahasiswa1.nama = "Eka putra gilang ramadhan"
mahasiswa1.jurusan = "Pendidilan Teknologi Informasi"
mahasiswa1.usia = 20
print(mahasiswa1.infoMahasiswa())