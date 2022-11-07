class Julkaisu:
    def __init__(self, name):
        self.julkaisun_nimi = name


class Lehti(Julkaisu):
    def __init__(self, toimittaja, name):
        self.paatoimittaja = toimittaja
        super().__init__( name)


    def tulosta_tiedot(self):
        print(self.julkaisun_nimi, self.paatoimittaja)

class Kirja(Julkaisu):
    def __init__(self, kirjailija, sivumaara, name):
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
        super().__init__( name)

    def tulosta_tiedot(self):
        print(self.julkaisun_nimi, self.kirjailija, self.sivumaara)


AkuAnkka = Lehti("AkiHyyppa","aku_ankka")

Hytti6 = Kirja("Rosa Liksom",200, "Hytti n:6")

AkuAnkka.tulosta_tiedot()
Hytti6.tulosta_tiedot()