class SivitasAkademik:

    def __init__(self, fakultas="", asaluniv = "", emailedu = ""):
        self.__fakultas = fakultas
        self.__asaluniv = asaluniv
        self.__emailedu = emailedu


    def getfakultas(self):
        return self.__fakultas

    def setfakultas(self, fakultas):
        self.__fakultas = fakultas

    def getasaluniv(self):
        return self.__asaluniv

    def setasaluniv(self, asaluniv):
        self.__asaluniv = asaluniv

    def getemailedu(self):
        return self.__emailedu

    def setemailedu(self, emailedu):
        self.__emailedu = emailedu