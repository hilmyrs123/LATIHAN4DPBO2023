class Course:

    def __init__(self, nama_matakuliah = ""):
        self.__nama_matakuliah = nama_matakuliah


    def getnama_matakuliah(self):
        return self.__nama_matakuliah
    
    def setnama_matakuliah(self, nama_matakuliah):
        self.__nama_matakuliah = nama_matakuliah