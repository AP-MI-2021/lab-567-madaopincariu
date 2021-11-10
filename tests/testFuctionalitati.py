from Domain.paine import getId, getLocatie, getNume, getDescriere
from Logic.CRUD import adaugaPaine, getById
from Logic.Functionalitati import pretMaxPerLocatie, concatenare, sumaPretPerLocatie, mutare, ordonareDupaPret


def testPretMaxPerLocatie():
    lista=[]
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista = adaugaPaine("3", "paine neagra", "germana", 7, "cuptor", lista)
    rezultat=pretMaxPerLocatie(lista)
    assert len(rezultat)==2
    assert rezultat["cuptor"]==7
    assert rezultat["raft"]==6

def testConcatenare():
    lista = []
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista = adaugaPaine("3", "paine neagra", "germana", 7, "cuptor", lista)
    lista = concatenare("abc", 5, lista)
    assert getDescriere(getById("1", lista)) == "frantuzeasca"
    assert getDescriere(getById("2", lista)) == "italianaabc"
    assert getDescriere(getById("3", lista)) == "germanaabc"

def testOrdonareDupaPret():
    lista = []
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista = adaugaPaine("3", "paine neagra", "germana", 7, "cuptor", lista)
    rezultat = ordonareDupaPret(lista)

    assert getId(rezultat[0])=="1"
    assert getId(rezultat[1]) =="2"
    assert getId(rezultat[2]) =="3"

def testSumaPretPerLocatie():
    lista = []
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista = adaugaPaine("3", "paine neagra", "germana", 7, "cuptor", lista)
    rezultat = sumaPretPerLocatie(lista)

    assert len(rezultat) == 2
    assert rezultat["cuptor"] == 11
    assert rezultat["raft"] == 6
def testMutare():
    lista = []
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista = adaugaPaine("3", "paine neagra", "germana", 7, "cuptor", lista)
    lista = mutare("cuptor", lista, "raft")

    assert getLocatie(getById("1", lista)) == "raft"
    assert getLocatie(getById("2", lista)) == "raft"
    assert getLocatie(getById("3", lista)) == "raft"