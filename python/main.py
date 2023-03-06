#import
from Mahasiswa import mahasiswa
from Dosen import Dosen
from SivitasAkademik import SivitasAkademik
from Course import Course
from ProgramStudi import ProgramStudi

#instansiasi
sivitas = SivitasAkademik()
course = Course()
mhs = mahasiswa()
dosen = Dosen()
prodi = ProgramStudi()

mahasiwa = []

#entry data
NIK = mhs.setNIK("01")
NIM = mhs.setNIM("2101")
nama = mhs.setnama("Ujang Van Houten")
jeniskelamin = mhs.setjeniskelamin("L")
fakultas = mhs.sivitas.setfakultas("FBTS")
asaluniv = mhs.sivitas.setasaluniv("University of Polopolo")
emailedu = mhs.sivitas.setemailedu("ujang@email.edu")
namaprodi = mhs.prodi.setnama_prodi("Teknik Sastra")
kodeprodi = mhs.prodi.setkode_prodi("TS01")
namamatkul = mhs.prodi.course.setnama_matakuliah("Rancangan Sirkuit Tata Bahasa")
mahasiwa.append(mhs(NIK, NIM, nama, jeniskelamin, fakultas, asaluniv,emailedu,
                    namaprodi, kodeprodi, namamatkul))

NIK = mhs.setNIK("02")
NIM = mhs.setNIM("2102")
nama = mhs.setnama("Rebecca Sutisna")
jeniskelamin = mhs.setjeniskelamin("P")
fakultas = mhs.sivitas.setfakultas("FMIA")
asaluniv = mhs.sivitas.setasaluniv("University of Polopolo")
emailedu = mhs.sivitas.setemailedu("beca@email.edu")
namaprodi = mhs.prodi.setnama_prodi("Pendidikan Matematika Syariah")
kodeprodi = mhs.prodi.setkode_prodi("PMS01")
namamatkul = mhs.prodi.course.setnama_matakuliah("Kalkulus Syariah")
mahasiwa.append(mhs(NIK, NIM, nama, jeniskelamin, fakultas, asaluniv,emailedu,
                    namaprodi, kodeprodi, namamatkul))

#print list
i = 0
print("list data : ")
for mhs in mahasiswa :
    print(str(i) + ".", mahasiswa.getNIK(), "|", mahasiswa.getnama(), 
          "|", mahasiswa.getjeniskelamin(), "|", mahasiswa.getNIM(),
          "|", mahasiswa.sivitas.getfakultas(), "|", mahasiswa.sivitas.getasaluniv,
          "|", mahasiswa.sivitas.getemailedu(), "|", mahasiswa.prodi.getnama_prodi(), "|",
          mahasiswa.prodi.getkode_prodi(), "|",mahasiswa.prodi.course.getnama_matakuliah())
    i += 1