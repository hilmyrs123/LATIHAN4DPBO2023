from Course import Course

class ProgramStudi:

    def __init__(self, nama_prodi = "", kode_prodi = ""):
        self.__nama_prodi = nama_prodi
        self.__kode_prodi = kode_prodi

        self.course = Course()

    def getnama_prodi(self):
        return self.__nama_prodi
    
    def setnama_prodi(self, nama_prodi):
        self.__nama_prodi = nama_prodi

    def getkode_prodi(self):
        return self.__kode_prodi
    
    def setkode_prodi(self, kode_prodi):
        self.__kode_prodi = kode_prodi
        