#import
from Mahasiswa import mahasiswa
from Dosen import Dosen

#instansiasi
mhs = mahasiswa()
dosen = Dosen()


list = []

#entry data
NIK = str(mhs.setNIK("01"))
NIM = str(mhs.setNIM("2101"))
nama = mhs.setnama("Ujang Van Houten")
jeniskelamin = mhs.setjeniskelamin("L")
fakultas = mhs.sivitas.setfakultas("FBTS")
asaluniv = mhs.sivitas.setasaluniv("University of Polopolo")
emailedu = mhs.sivitas.setemailedu("ujang@email.edu")
namaprodi = mhs.prodi.setnama_prodi("Teknik Sastra")
kodeprodi = mhs.prodi.setkode_prodi("TS01")
namamatkul = mhs.prodi.course.setnama_matakuliah("Rancangan Sirkuit Tata Bahasa")
list.append(mahasiswa(NIK, NIM, nama, jeniskelamin, fakultas,asaluniv, emailedu, namaprodi, kodeprodi, namamatkul))

NIK1 = mhs.setNIK("02")
NIM2 = mhs.setNIM("2102")
nama2 = mhs.setnama("Rebecca Sutisna")
jeniskelamin2 = mhs.setjeniskelamin("P")
fakultas2 = mhs.sivitas.setfakultas("FMIA")
asaluniv2 = mhs.sivitas.setasaluniv("University of Polopolo")
emailedu2 = mhs.sivitas.setemailedu("beca@email.edu")
namaprodi2 = mhs.prodi.setnama_prodi("Pendidikan Matematika Syariah")
kodeprodi2 = mhs.prodi.setkode_prodi("PMS01")
namamatkul2 = mhs.prodi.course.setnama_matakuliah("Kalkulus Syariah")

#dosen

dosen.setNIK("03")
dosen.setNIP("0121")
dosen.setnama("Aprodi Saprodi")
dosen.setjeniskelamin("L")
dosen.setpend_terakhir("S2")
dosen.setkeahlian("Menghitung Panjang Sajadah")
dosen.sivitas.setfakultas("FMIA")
dosen.sivitas.setasaluniv("University of Polopolo")
dosen.sivitas.setemailedu("aprodi@mail.edu")




#print list
i = 1
print("list data : ")
for mhs in list :
    print(str(i) + ".", mhs.getNIK(), "|", mhs.getNIM(), "|", mhs.getnama(), "|"
          , mhs.getjeniskelamin(), "|", mhs.sivitas.getfakultas(), "|", mhs.sivitas.getemailedu(), "|"
          , mhs.sivitas.getasaluniv(), "|", mhs.prodi.getkode_prodi(), "|", mhs.prodi.getnama_prodi())
    i += 1