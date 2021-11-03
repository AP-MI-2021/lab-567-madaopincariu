from Domain.paine import toString
from Logic.CRUD import adaugaPaine, stergePaine, modificaPaine
from Logic.Functionalitati import concatenare, pretMaxPerLocatie


def printMenu():
    print("1. Adaugare paine")
    print("2. Stergere paine")
    print("3. Modificare paine")
    print("4.Concatenarea unui string citit la toate descrierile painilor cu prețul mai mare decât o valoare citită.")
    print("5. Determinarea celui mai mare preț pentru fiecare locație.")
    print("a. Afisare paini")
    print("x. Iesire")

def uiAdaugaPaine(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input('Dati pretul: '))
        locatie = input("Dati locatia: ")
        return adaugaPaine(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiStergePaine(lista):
    try:
        id = input("Dati id-ul painii de sters: ")
        return stergePaine(id, lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiModificaPaine(lista):
    try:
        id = input("Dati id-ul painii de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input('Dati noul pret: '))
        locatie = input("Dati locatia: ")
        return modificaPaine(id, nume, descriere, pret,locatie, lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiConcatenare(lista):
    try:
        string=input("Dati un string: ")
        valoare=int(input("Dati o valoare: "))
        return concatenare(string,valoare,lista)
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiPretMaxPerLocatie(lista):
    rezultat= pretMaxPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie,rezultat[locatie]))

def showAll(lista):
    for paine in lista:
        print(toString(paine))

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaPaine(lista)
        elif optiune == "2":
            lista = uiStergePaine(lista)
        elif optiune == "3":
            lista = uiModificaPaine(lista)
        elif optiune =="4":
            lista=uiConcatenare(lista)
        elif optiune=="5":
            uiPretMaxPerLocatie(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")