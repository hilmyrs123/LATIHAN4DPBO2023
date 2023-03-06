from Human import Human
from SivitasAkademik import SivitasAkademik
from ProgramStudi import ProgramStudi

class Dosen(Human):

    def __init__(self, NIK="", nama="", jeniskelamin ="", NIP = "", pend_terakhir = "", keahlian = ""):
        super().__init__(NIK, nama, jeniskelamin)
        self.__NIP = NIP
        self.__pend_terakhir = pend_terakhir
        self.__keahlian = keahlian

        self.sivitas = SivitasAkademik()
        self.prodi = ProgramStudi()

    def getNIP(self):
        return self.__NIP

    def setNIP(self, NIP):
        self.__NIP = NIP

    def getpend_terakhir(self):
        return self.__pend_terakhir
    
    def setpend_terakhir(self, pend_terakhir):
        self.__pend_terakhir = pend_terakhir

    def getkeahlian(self):
        return self.__keahlian
    
    def setkeahlian(self, keahlian):
        self.__keahlian = keahlian

    
