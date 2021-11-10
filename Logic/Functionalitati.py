from Domain.paine import getPret, getId, getNume, getDescriere, getLocatie, creeazaPaine
from Logic.CRUD import adaugaPaine

def concatenare(string, valoare,lista):
    '''
    Concatenarea unui string citit la toate descrierile painilor cu prețul mai mare decât o valoare citită.
    :param string: un string dat
    :param valoare: o valoare data
    :param lista: lista de paini
    :return: lista de paini modificata
    '''
    if valoare<0:
        raise ValueError("Valoarea data trebuie sa fie un nr pozitiv")
    listaNoua=[]
    for paine in lista:
        if getPret(paine)> valoare:
            paineNoua=creeazaPaine(
                getId(paine),
                getNume(paine),
                getDescriere(paine)+string,
                getPret(paine),
                getLocatie(paine)
            )
            listaNoua.append(paineNoua)
        else:
            listaNoua.append(paine)
    return listaNoua

def pretMaxPerLocatie(lista):
    '''
     Determinarea celui mai mare preț pentru fiecare locație.
    :param lista: lista de paini
    :return: dictionar cu locatiile si preturile cele mai mari corespunzatoare fiecarei locatii
    '''
    rezultat={}
    for paine in lista:
        pret=getPret(paine)
        locatie=getLocatie(paine)
        if locatie in rezultat:
            if pret>rezultat[locatie]:
                rezultat[locatie]=pret
        else:
            rezultat[locatie]=pret
    return rezultat

def sumaPretPerLocatie(lista):
    '''
    Afisarea prețurilor pentru fiecare locație
    :param lista: lista de paini
    :return: sumele prețurilor pentru fiecare locație
    '''
    rezultat = {}
    for paine in lista:
        locatie = getLocatie(paine)
        if locatie in rezultat:
            rezultat[locatie] += getPret(paine)
        else:
            rezultat[locatie]=getPret(paine)
    return rezultat

def ordonareDupaPret(lista):
    '''
    Ordonarea obiectelor crescător după preț
    :param lista: lista de paini
    :return: lista de paini ordonata in functie de pret
    '''
    return sorted(lista, key=lambda paine: getPret(paine))

def mutare(locatieVeche, lista, locatieNoua):
    '''
    Mutarea tuturor obiectelor dintr-o locație în alta.
    :param locatieVeche: locatia initiala
    :param lista: lista de paini
    :return: lista modificata
    '''
    listaNoua=[]
    for paine in lista:
        if locatieVeche==getLocatie(paine):
            paineNoua=creeazaPaine(
                getId(paine),
                getNume(paine),
                getDescriere(paine),
                getPret(paine),
                getLocatie(paine).replace(getLocatie(paine), locatieNoua)
            )
            listaNoua.append(paineNoua)
        else:
            listaNoua.append(paine)
    return listaNoua

