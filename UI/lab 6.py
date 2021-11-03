
from Logic.CRUD import adaugaPaine, stergePaine, modificaPaine
from UI.Console import showAll

def help():
    '''
    Crearea unui nou meniu care foloseste comenzile: add, showall, delete, update
    '''
    print("Pentru a adauga o paine noua scrieti: add, id, nume, descriere, pret, locatie")
    print("Pentru a sterge o paine scrieti: delete, id")
    print("showall")
    print("Pentru a modifica o paine scrieti; update, id, nume, descriere, pret, locatie")
    print("stop")

def meniu(lista):
    while True:
        optiune = input("Introduceti o comanda: ")
        if optiune == "help":
            help()
        elif optiune == "stop":
            break
        else:
            actiune = optiune.split(";")
            for i in range(len(actiune)):
                comanda= actiune[i].split(",")
            for comanda in actiune:
                if comanda[0] == "add":
                    try:
                        lista = adaugaPaine(comanda[1], comanda[2], comanda[3] ,comanda[4], comanda[5], lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                        return lista
                elif comanda[0]== "help":
                    help()
                elif comanda[0] == "delete":
                    lista = stergePaine(comanda[1], lista)
                elif comanda[0] == "update":
                    try:
                        lista = modificaPaine(comanda[1], comanda[2], comanda[3], comanda[4], comanda[5], lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                        return lista
                elif comanda[0] == "showall":
                    showAll()