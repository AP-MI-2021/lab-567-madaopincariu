def creeazaPaine (id, nume, descriere, pret, locatie):
    '''
    creeaza o paine
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: un dictionar ce retine o paine
    '''
    return [id, nume, descriere, pret, locatie]

def getId(paine):
    '''
    ia id-ul painii
    :param paine: dictionar de tipul paine
    :return:id-ul painii
    '''
    return paine[0]
def getNume(paine):
    '''
    ia numele painii
    :param paine: dictionar de tipul paine
    :return: numele painii
    '''
    return paine[1]

def getDescriere(paine):
    '''
    ia descrierea painii
    :param paine: dictionar de tip paine
    :return: descrierea painii
    '''
    return paine[2]

def getPret(paine):
    '''
    ia pretul painii
    :param paine: dictionar de tip paine
    :return: pretul painii
    '''
    return paine[3]

def getLocatie(paine):
    '''
    ia locatia painii
    :param paine: dictionar de tip paine
    :return: locatia painii
    '''
    return paine[4]

def toString(paine):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(paine),
        getNume(paine),
        getDescriere(paine),
        getPret(paine),
        getLocatie(paine),
    )
