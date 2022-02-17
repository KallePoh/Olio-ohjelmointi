class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.

    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, *luvut):
        """Palauttaa kahden luvun summan.

        :param a: summan ensimmäinen luku
        :type a: Union[int, float]
        :param b: summan toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b summa
        :rtype: Union[int, float]
        """
        return sum([luvut[0], luvut[1]])

    def kerro(self, *luvut):
        """Palauttaa kahden luvun tulon.

        :param a: tulon ensimmäinen luku
        :type a: Union[int, float]
        :param b: tulon toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in [luvut[0], luvut[1]]:
            tulo *= luku
        return tulo


### Lisää MonenLaskija ja argumenttien_tulostaja tähän.



class MonenLaskija(Laskija):
    """Palauttaa kaikkien annettujen numeroitten summan


    :param luvut: Listassa olevat luvut
    :type luvut: Union[int, float]
    return: listan luvut lukujen summa 
    :rtype: Union[int, float]
    """
    
    def summaa(self, *luvut):
        summa = 0
        for number in luvut:
            summa += number
        return(summa)
    

    """Palauttaa kaikkien annettujen numeroitten tulon


    :param luvut: Listassa olevat luvut
    :type luvut: Union[int, float]
    return: listan luvut lukujen tulo 
    :rtype: Union[int, float]
    """
    
    def kerro(self, *luvut):
        tulo = 1
        for number in luvut:
            tulo = tulo * number
        return(tulo)
    





### Seuraavat rivit tekevät tarkistustulostukset. Älä koske niihin.

l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
# argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
# argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
