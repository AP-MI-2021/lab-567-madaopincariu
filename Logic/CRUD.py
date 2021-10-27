from Domain import paine
from Domain.paine import creeazaPaine, getId

def adaugaPaine(id, nume, descriere, pret, locatie,lista):
    '''
    adauga o paine la lista
    :param id: id-ul painii
    :param nume: numele painii
    :param descriere: descrierea painii
    :param pret: pretul painii
    :param locatie: locatia painii
    :param lista: lista de paini
    :return: lista cu noua paine adaugata
    '''
    paine=creeazaPaine(id, nume, descriere, pret, locatie)
    return lista + [paine]

def stergePaine(id, lista):
    '''
    sterge o paine din lista
    :param id: id-ul painii
    :param lista: lista de paini
    :return: lista fara painea stearsa
    '''
    return [paine for paine in lista if getId(paine)!=id]


def creazaPaine(id, nume, descriere, pret, locatie):
    pass

def modificaPaine(id, nume, descriere, pret, locatie,lista):
    '''
    modifica o lista de paini
    :param id: id-ul painii
    :param nume: numele painii
    :param descriere: descrierea painii
    :param pret: pretul painii
    :param locatie: locatia painii
    :param lista: lista de paini
    :return: o lista de paini modificata
    '''
    listaNoua=[]
    if getId(paine)==id:
        paineNoua= creazaPaine(id, nume, descriere, pret, locatie)
        listaNoua.append(paineNoua)
    else:
        listaNoua.append(paine)
    return listaNoua

def getById(id,lista):
    '''
    :param id: id-ul painii
    :param lista: lista de paini
    :return:
    '''
    for paine in lista:
        if getId(paine)==id:
            return paine
    return None