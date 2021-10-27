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
    return {
        'id':id,
        'nume':nume,
        'descriere':descriere,
        'pret':pret,
        'locatie':locatie
    }
def getId(paine):
    '''
    ia id-ul painii
    :param paine: dictionar de tipul paine
    :return:id-ul painii
    '''
    return paine["id"]
def getNume(paine):
    '''
    ia numele painii
    :param paine: dictionar de tipul paine
    :return: numele painii
    '''
    return paine["nume"]

def getDescriere(paine):
    '''
    ia descrierea painii
    :param paine: dictionar de tip paine
    :return: descrierea painii
    '''
    return paine["descriere"]

def getPret(paine):
    '''
    ia pretul painii
    :param paine: dictionar de tip paine
    :return: pretul painii
    '''
    return paine["pret"]

def getLocatie(paine):
    '''
    ia locatia painii
    :param paine: dictionar de tip paine
    :return: locatia painii
    '''
    return paine["locatie"]

def toString(paine):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(paine),
        getNume(paine),
        getDescriere(paine),
        getPret(paine),
        getLocatie(paine),
    )
