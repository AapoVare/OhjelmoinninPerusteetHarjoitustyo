"""
Tekijä: Aapo Väre
Ryhmä:TTV20S2
Tehtävä: Harjoitustyö
Kuvaus:
    Ohjelmassa luodaan käyttäjätunnus ja salasana, joita voidaan sitten käyttää sisäänkirjautumista varten.
    Luotuaan käyttäjätunnuksen, ohjelma tallettaa käyttäjänmiet ja salasanat kahteen erilliseen tekstitiedostoon.

    Alunperin oli tarkoitus saada aikaan myös toteutus, jossa ohjelma lukee tekstitiedostojen sisällön,
    jolloin sisäänkirjautuminen onnistuisi myös niissä olevilla tiedoilla, mutta en saanut sitä onnistumaan.
"""
from getpass import getpass
käyttäjät = {}
status = ""
luodut_tunnukset = []
tunnus_luku = "tunnukset.txt"
salasana_luku = "salasanat.txt"
try:
    tunnukset_file = open ("tunnukset.txt", "x") 
    salasanat_file = open ("salasanat.txt", "x") # Luovat tiedostot jos niitä ei ole olemassa
except:
    tunnukset_file = open ("tunnukset.txt", "a") 
    salasanat_file = open ("salasanat.txt", "a") # Jos tiedostot ovat olemassa, nämä avaavat ne appending tilaan, missä niiden tietoja ei ylikirjoiteta

"""
Tässä on epäonnistunut aliohjelma, jonka piti suorittaa tiedostojen lukeminen.
def TiedostonLuku(käyttäjä):
    file = open(tunnus_luku, "r")
    if luku1 in tunnus_luku:
        luku1.append(käyttäjät)
    file2 = open(salasana_luku, "r")
    if luku2 in salasana_luku:
        luku2.append(käyttäjät)
"""
# Lue tällä tiedostosta onko käyttäjänimi ja salasana jo olemassa, käytä uusikäyttäjässä kun luodaan käyttäjänimeä ja vanhakäyttäjässä kirjautumisen jälkeen
# Jos syötetyt tunnukset löytyy tiedostosta niin ohjelman pitää onnistua niilläkin


def StarttiMenu(): # Tässä aloitusmenu, joka kysyy onko käyttäjätunnus jo rekisteröity vai ei
    status = str(input("Oletko rekisteröity käyttäjä? k/e? Paina q lopettaaksesi: "))

    if status == "k":
        return VanhaKäyttäjä()
    elif status == "e":
        UusiKäyttäjä()
    elif status == "q":
        return status
    elif status != "q" or "k" or "e":
        print("Virheellinen syöte!")

def UusiKäyttäjä(): # Tässä luodaan uusi käyttäjätunnus ja kirjoitetaan käyttäjänimi ja salasana erillisiin tiedostoihin
    virhe_tunnus = ""
    virhe_sala = ""
    while virhe_tunnus != "ok":  # Looppaa alkuun jos käyttäjänimi on varattu
        LuoTunnus = input("Luo käyttäjänimi: ")
        if LuoTunnus in käyttäjät:
            print("Käyttäjänimi on varattu!")
        else:
            virhe_tunnus = "ok"
            luodut_tunnukset.append(LuoTunnus) # Lisää luodun tunnuksen luotujen tunnuksien listaan
            while virhe_sala != "ok": # Looppaa takaisin salasanan luontiin, jos salasanat eivät täsmää
                tunnukset_file.write(str(LuoTunnus) + "\n") # kirjoittaa uuden tunnuksen tunnustiedostoon
                LuoSalasana = getpass("Luo salasana: ") #Tämä piilottaa syötteen, mutta säilyttää silti muuttujan arvon
                vahvistus = getpass("Vahvista salasana: ")
                if vahvistus == LuoSalasana:
                    salasanat_file.write(str(LuoSalasana) + "\n") # kirjoittaa uuden salasanan salasanatiedostoon
                    käyttäjät[LuoTunnus] = LuoSalasana
                    print ("Tunnus luotu!")
                    print("Käyttäjänimi: ", LuoTunnus)
                    print ("Salasana: ", len(LuoSalasana)*"*")
                    virhe_sala = "ok"
                else:
                    print("Salasanat eivät täsmää!")

def VanhaKäyttäjä(): # Tässä Kirjaudutaan sisään jo olemassa olevilla tunnuksilla
    for i in range(1,4):
        tunnus = input("Syötä käyttäjänimi: ")
        salasana = input("Syötä salasana: ")
        if tunnus in käyttäjät and käyttäjät[tunnus] == salasana:
            print("Tervetuloa ", tunnus,"!")
            status_end = ""
            while status_end != "q": # tämä osio on tässä, jos tulevaisuudessa ohjelmaan haluaa lisätä valikko-toiminnon, toistaiseksi looppaa niin kauan kunnes käyttäjä painaa q
                # tulosta uusi menu
                status_end = input("Haluatko aloittaa ohjelman alusta? Paina q lopettaaksesi: ")
                # riippuen statuksesta/inputista, tee funktio
            return status_end
            break
        else:
            print("Väärä tunnus tai salasana!")
    print("Liian monta väärää yritystä!")
    status = "q"
    return status
while True: # looppaa ohjelmaa niin kauan, kunnes käyttäjä syöttää q ohjelman sitä kysyessä
    status = StarttiMenu()
    if (status == "q"):
        break

tunnukset_file.close()
salasanat_file.close()
if luodut_tunnukset != []: # Jos luotujen tunnuksien lista ei ole tyhjä, luodut tunnukset tulostetaan
    print("Seuraavat käyttäjätunnukset luotu: ", luodut_tunnukset)
print ("Hyvää päivänjatkoa!")

# Ohjelma päättyy