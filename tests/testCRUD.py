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

    lista = modificaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)

    paineUpdatata = getById("1", lista)
    assert getId(paineUpdatata) == "1"
    assert getNume(paineUpdatata) == "bagheta"
    assert getDescriere(paineUpdatata) == "frantuzeasca"
    assert getPret(paineUpdatata) == 4
    assert getLocatie(paineUpdatata) == "cuptor"

    paineNeupdatata = getById("2", lista)
    assert getId(paineNeupdatata) == "2"
    assert getNume(paineNeupdatata) == "franzela"
    assert getDescriere(paineNeupdatata) == "italiana"
    assert getPret(paineNeupdatata) == 6
    assert getLocatie(paineNeupdatata) == "raft"

    lista = []
    lista = adaugaPaine("1", "bagheta", "frantuzeasca", 4, "cuptor", lista)

    lista = modificaPaine("3", "crestata", "germana",7 ,"raft", lista)

    paineNeupdatata = getById("1", lista)
    assert getId(paineNeupdatata) == "1"
    assert getNume(paineNeupdatata) == "bagheta"
    assert getDescriere(paineNeupdatata) == "frantuzeasca"
    assert getPret(paineNeupdatata) == 4
    assert getLocatie(paineNeupdatata) == "cuptor"