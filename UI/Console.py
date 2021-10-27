from Domain.paine import toString
from Logic.CRUD import adaugaPaine, stergePaine, modificaPaine

def printMenu():
    print("1. Adaugare paine")
    print("2. Stergere paine")
    print("3. Modificare paine")
    print("a. Afisare paini")
    print("x. Iesire")

def uiAdaugaPaine(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = float(input('Dati pretul: '))
    locatie = input("Dati locatia: ")
    return adaugaPaine(id, nume, descriere, pret, locatie, lista)

def uiStergePaine(lista):
    id = input("Dati id-ul painii de sters: ")
    return stergePaine(id, lista)

def uiModificaPaine(lista):
    id = input("Dati id-ul painii de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input('Dati noul pret: '))
    locatie = input("Dati locatia: ")
    return modificaPaine(id, nume, descriere, pret,locatie, lista)

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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")