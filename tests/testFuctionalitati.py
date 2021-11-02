from Logic.CRUD import adaugaPaine
from Logic.Functionalitati import pretMaxPerLocatie


def testPretMaxPerLocatie():
    lista=[]
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista = adaugaPaine("3", "paine neagra", "germana", 7, "cuptor", lista)
    rezultat=pretMaxPerLocatie(lista)
    assert len(rezultat)==2
    assert rezultat["cuptor"]==7
    assert rezultat["raft"]==6