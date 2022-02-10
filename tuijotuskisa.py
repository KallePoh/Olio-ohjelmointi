import random
import time


class Olento:
    def __init__(self):
        self.rohkeus = random.randint(4, 8)
        self.katseen_voima = random.randint(2, 4)
    
    

"""Palauttaa satunnaisen hurraushuudahduksen.

    :return: hurraava huudahdus
    :rtype: str
        
    
    
    :ivar rohkeus: olennon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: olennon katseen voimakkuus, arvotaan
    :type katseen_voima: int
    """



class Peikko(Olento):
    """Luokka, joka kuvaa Peikon.

    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    
    
    Julkiset metodit
        arvo_hurraus()pl
    """
    
    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    def __init__(self):
        """Konstruktori."""
        self.nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        super().__init__()

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)

    


class Vuorenpeikko(Peikko):
    NIMITAVUT = ("Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")
    RIEMUTAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan",)
    
    def __init__(self):
        self.nimi = self._arvo_sanat(self.RIEMUTAVUT, 3, "-")
        super().__init__()
        #Arvotaan Luolapeikon rohkeus
        self.rohkeus = random.randint(2, 4)
        #Arvotaan Luolapeikon katseen voima
        self.katseen_voima = random.randint(1, 2)
    
    #Arvotaan Vuoripeikon hurraus
    def arvo_hurraus(self):
        
        return self._arvo_sanat(self.NIMITAVUT, 8, " ", 0.7)
    


class Luolapeikko(Peikko):
    NIMITAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar",)
    RIEMUTAVUT = ("Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    
   

    def __init__(self):
        self.nimi = self._arvo_sanat(self.RIEMUTAVUT, 3, "-")
        super().__init__()
        #Arvotaan Luolapeikon rohkeus
        self.rohkeus = random.randint(5, 10)
        #Arvotaan Luolapeikon katseen voima
        self.katseen_voima = random.randint(3, 6)

        # Arvotaan Luolapeikon hurraus
    def arvo_hurraus(self):
        return self._arvo_sanat(self.NIMITAVUT, 8, " ", 0.7)


class Sankari(Olento):
    """Luokka, joka kuvaa Sankarin.

    :ivar nimi: sankarin nimi, kysytään käyttäjältä
    :type nimi: str
    
    
    Julkiset metodit
        arvo_hurraus()
    """
    
    
    def __init__(self, nimi):
        self.nimi = nimi
        super().__init__()
        

    

    def arvo_hurraus(self):
        """
        Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        HURRAUKSET = ["Jes!", "Let's Go!", "Hurraa!", "Jeee!", "Jippii!"]
        return random.choice(HURRAUKSET)

def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.

    :param olio: hurraava olio
    """
    print(f'{olio.nimi}: "{olio.arvo_hurraus()}!"')


def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.

    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print(f"ja {rapayttaja.nimi} räpäyttää!")
        else:
            print(f"ja {rapayttaja.nimi} karkaa!")
    else:
        print("eikä kummankaan silmä rävähdä!")


def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea




        
sankari = Sankari(input("Mikä on sankarimme nimi? "))
pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print(f"Sankarimme {sankarin_tiedot} kävelee kohti seikkailua.")
    time.sleep(0.7)

    # Tulostetaan vastaan tulevan peikon tiedot.

    """Arvotaan minkälainen peikko luodaan"""
    peikko_valinta = random.randint(1, 3)
    if peikko_valinta == 1:
        peikko = Peikko()
    elif peikko_valinta == 2:
        peikko = Luolapeikko()
    else:
        peikko = Vuorenpeikko()
    
    peikon_tiedot = peikko.nimi + " [" + str(peikko.rohkeus) + "]"
    print(f"Vastaan tulee hurja {peikon_tiedot}!")
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print(f"{sankari.nimi} herää sängystään hikisenä - onneksi se oli vain unta!")
