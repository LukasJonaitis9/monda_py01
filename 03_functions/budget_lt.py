""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas  +++
* Spausdinti pajamų/išlaidų žurnalą+++
* Suskaičiuoti biudžeto balansą 

"""
### BIUDZETAS

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