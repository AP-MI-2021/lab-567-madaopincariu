from Domain.paine import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaPaine, stergePaine, getById, modificaPaine

def testAdaugaPaine():
    lista=[]
    lista= adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor",lista)
    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "bagheta"
    assert getDescriere(lista[0]) == "frantuzeasca"
    assert getPret(lista[0]) == 4
    assert getLocatie(lista[0]) == "cuptor"

def testStergePaine():
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", [])
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista=stergePaine("1", lista)
    assert len(lista)==1
    assert getById("1",lista) is None

    lista = stergePaine("3", lista)
    assert len(lista) == 1
    assert getById("2",lista) is not None

def testModificaPaine():
    lista = []
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)
    lista = adaugaPaine("2", "franzela", "italiana", 6, "raft", lista)
    lista = modificaPaine("1", "paine neagra", "germana", 7, "cuptor", lista)

    paine_actualizata = getById("1", lista)

    assert getId(paine_actualizata) == "1"
    assert getNume(paine_actualizata) == "paine neagra"
    assert getDescriere(paine_actualizata) == "germana"
    assert getPret(paine_actualizata) == 7
    assert getLocatie(paine_actualizata) == "cuptor"

    assert getId(getById("2", lista)) == "2"
    assert getNume(getById("2", lista)) == "franzela"
    assert getDescriere(getById("2", lista)) == "italiana"
    assert getPret(getById("2", lista)) == 6
    assert getLocatie(getById("2", lista)) == "raft"