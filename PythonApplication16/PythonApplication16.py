from datetime import *

def kylg():
    Kylg1 = int(input("Sisesta 1 kylje pikkus"))
    Kylg2 = int(input("Sisesta 2 kylje pikkus"))
    Kylg3 = int(input("Sisesta 3 kylje pikkus"))
    Kylg4 = int(input("Sisesta 4 kylje pikkus"))

    if Kylg1 <= 0 or Kylg2 <= 0 or Kylg3 <= 0 or Kylg4 <= 0:
        print("Arv peab olema positiivine")
    else:
        try:
            if Kylg1 == Kylg2 == Kylg3 == Kylg4:
                print("Sul on ruut")
            else:
                print("Sul ei ole ruut")
        except ValueError:
            print("Viga")


def kalk():
    try:
        arv1 = int(input("Sisesta arv 1"))
        arv2 = int(input("Sisesta arv 2"))
        tehe = input("Mis tehet tahad teha? (+, -, *, /)")

        if tehe == "+":
            print("Vastus:", arv1 + arv2)
        elif tehe == "-":
            print("Vastus:", arv1 - arv2)
        elif tehe == "*":
            print("Vastus:", arv1 * arv2)
        elif tehe == "/":
            if arv1 != 0 or arv2 != 0:
                print("Vastus:", arv1 / arv2)
            else:
                print("Nulli jagamis viga")
    except ValueError:
            print("Viga")

def aasta():
    vanus = int(input("Sisesta enda synni aasta"))
    aeg = date.today().year - vanus

    print("Saad", aeg, "aastaseks")
    if vanus % 5 == 0 or vanus % 10 == 0:
        print("Sul on juubel")
    else:
        print("Sul ei ole juubel")


def pood():
    hind = float(input("Sisesta toote hind: "))

    if hind <= 10:
        hna = hind * 0.10
        print("Teie allahindlus on 10%, ja peate maskma:", hind - hna)
    elif hind >= 20:
        hna = hind * 0.20
        print("Teie allahindlus on 20%, ja peate maskma:", hind - hna)

def jalgpall():
    sugu = input("Kas oled mees voi naine")
    sugu = sugu.lower()
    if sugu == "naine":
        print("Sorri, aga te ei sobi meile")
    elif sugu == "mees":
        vanus = int(input("Mis on teie vanus?"))
        if 16 <= vanus <= 18:
            print("Sobid meilse")
        elif vanus < 16:
            print("Oled liiga noor")
        else:
            print("Oled liiga vana")
    else:
        print("Vasta kysimusele")

def kohad():
    inimarv = int(input("Mitu inimest vajab bussi? "))
    buss = 50

    bussid = inimarv // buss

    leftover = inimarv % buss

    print("Vaja laheb", bussid, "tais bussi")
    print("Yle jaab", leftover, "inimest")