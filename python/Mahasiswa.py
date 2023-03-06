from Human import Human
from SivitasAkademik import SivitasAkademik
from ProgramStudi import ProgramStudi

class mahasiswa(Human):

    def __init__(self, NIK="", nama="", jeniskelamin ="", NIM = "", fakultas = ""
                 , asaluniv = "", emailedu = "", nama_prodi = "", kode_prodi = "", 
                 nama_matakuliah = ""):
        super().__init__(NIK, nama, jeniskelamin)
        self.__NIM = NIM

        self.sivitas = SivitasAkademik()
        self.sivitas.__fakultas = fakultas
        self.sivitas.__asaluniv = asaluniv
        self.sivitas.__emailedu = emailedu

        self.prodi = ProgramStudi()
        self.prodi.__kode_prodi = kode_prodi
        self.prodi.__nama_prodi = nama_prodi

        self.prodi.course.__nama_matakuliah = nama_matakuliah


    def getNIM(self):
        return self.__NIM

    def setNIM(self, NIM):
        self.__NIM = NIM
