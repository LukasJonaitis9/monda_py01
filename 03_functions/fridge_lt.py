""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""
def prideti_pajamas(biudzetas, paskirtis, suma):
    if paskirtis not in biudzetas:
        biudzetas[paskirtis] = 0
    biudzetas[paskirtis] += suma
    return biudzetas

def prideti_islaidas(biudzetas, paskirtis, suma):
    if paskirtis not in biudzetas:
        biudzetas[paskirtis] = 0
    biudzetas[paskirtis] -= suma
    return biudzetas

def spausdinti_zurnala(biudzetas):
    print("Pajamų/Išlaidų Žurnalas:")
    for paskirtis, suma in biudzetas.items():
        print(f"{paskirtis}: {suma}")

def skaiciuoti_balansa(biudzetas):
    balansas = sum(biudzetas.values())
    print(f"Bendra Pajamų/Išlaidų Balansas: {balansas}")

biudzetas = {}

while True:
    print('=-=-=Biudžetas=-=-=')
    print('0: Išeiti')
    print('1: Pridėti pajamas')
    print('2: Pridėti išlaidas')
    print('3: Spausdinti žurnalą')
    print('4: Skaiciuoti balansą')
    pasirinkimas = input('Pasirinkimas: ')

    if pasirinkimas == '0':
        break
    elif pasirinkimas == '1':
        paskirtis = input('Pajamų paskirtis: ')
        suma = float(input('Suma: '))
        biudzetas = prideti_pajamas(biudzetas, paskirtis, suma)
    elif pasirinkimas == '2':
        paskirtis = input('Išlaidų paskirtis: ')
        suma = float(input('Suma: '))
        biudzetas = prideti_islaidas(biudzetas, paskirtis, suma)
    elif pasirinkimas == '3':
        spausdinti_zurnala(biudzetas)
    elif pasirinkimas == '4':
        skaiciuoti_balansa(biudzetas)
    else:
        print('Neteisingas pasirinkimas. Bandykite dar kartą.')