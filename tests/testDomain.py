from Domain.paine import creeazaPaine, getId , getNume, getDescriere, getPret, getLocatie

def testPaine():
    paine = creeazaPaine("1","bagheta","frantuzeasca",4,"cuptor")
    assert getId(paine) == "1"
    assert getNume(paine) == "bagheta"
    assert getDescriere(paine) == "frantuzeasca"
    assert getPret(paine) == 4
    assert getLocatie(paine) == "cuptor"
