from Domain.paine import toString
from Logic.CRUD import adaugaPaine, stergePaine, modificaPaine
from Logic.Functionalitati import concatenare, pretMaxPerLocatie, ordonareDupaPret, sumaPretPerLocatie, mutare


def printMenu():
    print("1. Adaugare paine")
    print("2. Stergere paine")
    print("3. Modificare paine")
    print("4. Concatenarea unui string citit la toate descrierile painilor cu prețul mai mare decât o valoare citită.")
    print("5. Determinarea celui mai mare preț pentru fiecare locație.")
    print("6. Ordonarea obiectelor crescător după preț.")
    print("7. Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u. Undo.")
    print("r. Redo.")
    print("a. Afisare paini")
    print("x. Iesire")

def uiAdaugaPaine(lista,undoList,redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input('Dati pretul: '))
        locatie = input("Dati locatia: ")
        rezultat= adaugaPaine(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiStergePaine(lista, undoList,redoList):
    try:
        id = input("Dati id-ul painii de sters: ")
        rezultat= stergePaine(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiModificaPaine(lista,undoList,redoList):
    try:
        id = input("Dati id-ul painii de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input('Dati noul pret: '))
        locatie = input("Dati locatia: ")
        rezultat= modificaPaine(id, nume, descriere, pret,locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiConcatenare(lista,undoList,redoList):
    try:
        string=input("Dati un string: ")
        valoare=int(input("Dati o valoare: "))
        rezultat= concatenare(string,valoare,lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print ("Eroare: {}".format(ve))
        return lista

def uiPretMaxPerLocatie(lista):
    rezultat= pretMaxPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie,rezultat[locatie]))
def uiOrdonareDupaPret(lista):
    showAll(ordonareDupaPret(lista))

def uiSumaPretPerLocatie(lista):
    rezultat = sumaPretPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))

def uiMutare(lista,undoList,redoList):
    locatieVeche=input("Dati locatia care doriti sa fie schimbata:")
    locatieNoua=input("Dati noua locatie: ")
    rezultat= mutare(locatieVeche, lista, locatieNoua)
    undoList.append(lista)
    redoList.clear()
    return rezultat

def showAll(lista):
    for paine in lista:
        print(toString(paine))

def runMenu(lista):
    undoList=[]
    redoList=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaPaine(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergePaine(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaPaine(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiConcatenare(lista, undoList, redoList)
        elif optiune == "5":
            uiPretMaxPerLocatie(lista)
        elif optiune == "6":
            uiOrdonareDupaPret(lista)
        elif optiune == "8":
            uiSumaPretPerLocatie(lista)
        elif optiune=="7":
            uiMutare(lista,undoList,redoList)
        elif optiune=="u":
            if len(undoList)>0:
                redoList.append(lista)
                lista=undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune=="r":
            if len(redoList)>0:
                undoList.append(lista)
                lista=redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")