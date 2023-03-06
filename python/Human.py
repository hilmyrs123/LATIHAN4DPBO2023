class Human:

    def __init__(self, NIK = "", nama = "", jeniskelamin = ""):
        self.__NIK = NIK
        self.__nama = nama
        self.__jeniskelamin = jeniskelamin

    def getNIK(self):
        return self.__NIK

    def setNIK(self, NIK):
        self.__NIK = NIK

    def getnama(self):
        return self.__nama

    def setnama(self, nama):
        self.__nama = nama

    def getjeniskelamin(self):
        return self.__jeniskelamin

    def setjeniskelamin(self, jeniskelamin):
        self.__jeniskelamin = jeniskelamin