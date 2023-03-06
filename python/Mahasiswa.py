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
        self.prodi = ProgramStudi()


    def getNIM(self):
        return self.__NIM

    def setNIM(self, NIM):
        self.__NIM = NIM
