""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""




######## PASTABOS 
def sukurti_albuma(atlikejas, pavadinimas):
    return {'atlikejas': atlikejas, 'pavadinimas': pavadinimas, 'takeliai': []}

def prideti_takeli(albumas, eile, pavadinimas, trukme):
    albumas['takeliai'].append({'eile': eile, 'pavadinimas': pavadinimas, 'trukme': trukme})
    return albumas

def redaguoti_albuma(albumas, atlikejas=None, pavadinimas=None):
    if atlikejas:
        albumas['atlikejas'] = atlikejas
    if pavadinimas:
        albumas['pavadinimas'] = pavadinimas
    return albumas

def redaguoti_takeli(albumas, eile, pavadinimas=None, trukme=None):
    for takelis in albumas['takeliai']:
        if takelis['eile'] == eile:
            if pavadinimas:
                takelis['pavadinimas'] = pavadinimas
            if trukme:
                takelis['trukme'] = trukme
            return albumas
    print(f"Takelis su eile {eile} nerastas.")
    return albumas

def trinti_takeli(albumas, eile):
    albumas['takeliai'] = [takelis for takelis in albumas['takeliai'] if takelis['eile'] != eile]
    return albumas

def perziureti_albuma(albumas):
    print(f"Atlikėjas: {albumas['atlikejas']}")
    print(f"Pavadinimas: {albumas['pavadinimas']}")
    print(f"Takelių kiekis: {len(albumas['takeliai'])}")
    trukmes_sekundemis = sum([takelis['trukme'] for takelis in albumas['takeliai']])
    trukmes_min_sek = f"{trukmes_sekundemis // 60}:{trukmes_sekundemis % 60:02}"
    print(f"Bendra trukmė: {trukmes_min_sek}")

def perziureti_dainas(albumas):
    print("Dainų sąrašas:")
    for takelis in sorted(albumas['takeliai'], key=lambda x: x['eile']):
        trukme_min_sek = f"{takelis['trukme'] // 60}:{takelis['trukme'] % 60:02}"
        print(f"{takelis['eile']}. {takelis['pavadinimas']} - {trukme_min_sek}")

atlikejas = {}

def iseiti():
    print("Programa baigia darbą.")
    exit()

def main():
    mano_albumas = None  # Bus naudojamas kaip albumo kintamasis

    while True:
        print("\n=-=-= Meniu =-=-=")
        print("0: Išeiti")
        print("1: Sukurti albumą")
        print("2: Pridėti takelį")
        print("3: Redaguoti albumą")
        print("4: Redaguoti takelį")
        print("5: Trinti takelį")
        print("6: Peržiūrėti albumą")
        print("7: Peržiūrėti dainas")

        pasirinkimas = input("Įveskite pasirinkimą: ")

        if pasirinkimas == '0':
            iseiti()
        elif pasirinkimas == '1':
            atlikejas = input("Įveskite atlikėją: ")
            pavadinimas = input("Įveskite pavadinimą: ")
            mano_albumas = sukurti_albuma(atlikejas, pavadinimas)
            print("Albumas sukurtas.")
        elif pasirinkimas == '2':
            if mano_albumas:
                eile = int(input("Įveskite dainos eilės numerį: "))
                pavadinimas = input("Įveskite dainos pavadinimą: ")
                trukme = int(input("Įveskite dainos trukmę sekundėmis: "))
                mano_albumas = prideti_takeli(mano_albumas, eile, pavadinimas, trukme)
                print("Takelis pridėtas.")
            else:
                print("Sukurkite albumą pirmiau.")
        elif pasirinkimas == '3':
            if mano_albumas:
                atlikejas = input("Įveskite naują atlikėją (jei nekeisite, spauskite Enter): ")
                pavadinimas = input("Įveskite naują pavadinimą (jei nekeisite, spauskite Enter): ")
                mano_albumas = redaguoti_albuma(mano_albumas, atlikejas, pavadinimas)
                print("Albumo informacija atnaujinta.")
            else:
                print("Sukurkite albumą pirmiau.")
        elif pasirinkimas == '4':
            if mano_albumas:
                eile = int(input("Įveskite takelio eilės numerį: "))
                pavadinimas = input("Įveskite naują takelio pavadinimą (jei nekeisite, spauskite Enter): ")
                trukme = int(input("Įveskite naują takelio trukmę sekundėmis (jei nekeisite, spauskite Enter): "))
                mano_albumas = redaguoti_takeli(mano_albumas, eile, pavadinimas, trukme)
                print("Takelio informacija atnaujinta.")
            else:
                print("Sukurkite albumą pirmiau.")
        elif pasirinkimas == '5':
            if mano_albumas:
                eile = int(input("Įveskite takelio eilės numerį, kurį norite ištrinti: "))
                mano_albumas = trinti_takeli(mano_albumas, eile)
                print("Takelis ištrintas.")
            else:
                print("Sukurkite albumą pirmiau.")
        elif pasirinkimas == '6':
            if mano_albumas:
                perziureti_albuma(mano_albumas)
            else:
                print("Sukurkite albumą pirmiau.")
        elif pasirinkimas == '7':
            if mano_albumas:
                perziureti_dainas(mano_albumas)
            else:
                print("Sukurkite albumą pirmiau.")
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

if __name__ == "__main__":
    main()