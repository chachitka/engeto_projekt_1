"""
projekt_1.py: První projekt do Engeto Online Python Akademie
autor: Lenka Krčmáriková
email: l.krcmarikova@seznam.cz
discord: lenka_34840
"""

jmena_hesla = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

user_jmeno = input("Zadej své uživatelské jméno:").lower()
user_heslo = input("Zadej své heslo:")

oddelovac = "-" * 47

print(oddelovac)

if user_jmeno in jmena_hesla and jmena_hesla.get(user_jmeno) == user_heslo:
    print(f"Ahoj, {user_jmeno.capitalize()}, vítej v aplikaci 'Analýza textu'.")
    print("Máme tři texty k analýze.")
    print(oddelovac)    


    text = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


    volba = input("Vyber možnost (1-3): ")

    if volba in ["1", "2", "3"]:
        index = int(volba) - 1
        print(oddelovac)
        print(f"Analýza textu č. {volba}:")

        novy_text = text[index].replace(".", "").replace(",", "")
        slova = novy_text.split()

        delka_text = len(slova)
        print(f"Ve vybraném textu je celkem {delka_text} slov.")
        
        pocet_titlecase = 0
        pocet_uppercase = 0
        pocet_lowercase = 0
        pocet_digit = 0
        cisla = []
        delka_slov = []

        for slovo in slova:
            if slovo.istitle():
                pocet_titlecase += 1
            if slovo.isupper() and slovo.isalpha():
                pocet_uppercase += 1
            if slovo.islower():
                pocet_lowercase += 1
            if slovo.isdigit():
                pocet_digit += 1
                cisla.append(int(slovo))
            delka_slov.append(len(slovo))

        pocet_vyskyt = {}
        for delka in delka_slov:
            if delka not in pocet_vyskyt:
                pocet_vyskyt[delka] = 1
            else:
                pocet_vyskyt[delka] += 1

        print(f"Počet slov s počátečním velkým písmenem je {pocet_titlecase}.")
        print(f"Počet slov s velkými písmeny je {pocet_uppercase}.")
        print(f"Počet slov s malými písmeny je {pocet_lowercase}.")
        print(f"Počet čísel v textu je {pocet_digit}.")
        print(f"Suma všech čísel v textu činí {sum(cisla)}.")
       
        print(oddelovac)
        
        max_delka = len(str(max(pocet_vyskyt.keys())))
        max_stars = max(pocet_vyskyt.values())

        print(
            f"{'Délka':<{max_delka}} | "
            f"{'Výskyt'.center(max_stars + 2)} | "
            f"{'Počet'}"
        )
        
        print(oddelovac)
        
        pocet_vyskyt_sorted = sorted(pocet_vyskyt.items())
        for key, value in pocet_vyskyt_sorted:
            stars = ('*' * value)
            print(
                f"{key:{max_delka + 3}} | "
                f"{stars:<{max_stars + 2}} |"
                f"{value}"
            )
    else:
        print("Neplatná volba. Zvolte prosím číslo mezi 1 a 3.")
else:
    print("Uživatel není registrován, aplikace bude ukončena...")
