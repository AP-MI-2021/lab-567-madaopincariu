from Domain.paine import getPret, getId, getNume, getDescriere, getLocatie
from Logic.CRUD import adaugaPaine

def concatenare(string, valoare,lista):
    '''
    Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    :param string: un string dat
    :param valoare: o valoare data
    :param lista: lista de paini
    :return: lista de paini modificata
    '''
    listaNoua=[]
    for paine in lista:
        if getPret(paine)> valoare:
            paineNoua=adaugaPaine(
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

