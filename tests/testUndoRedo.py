from Logic.CRUD import adaugaPaine

def test_undo_redo():
    lista = []
    undoList = []
    redoList = []

    undoList.append(lista)
    redoList.clear()

    lista = adaugaPaine("1", "franzela", "italiana", 5, "raft", lista)

    undoList.append(lista)
    redoList.clear()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'}]

    lista = adaugaPaine("2", "bagheta", "frantuzeasca", 4, "cuptor", lista)

    undoList.append(lista)
    redoList.clear()

    lista = adaugaPaine("3", "chifla", "greceasca", 6, "raft", lista)

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '2', 'nume': 'bagheta', 'descriere': 'frantuzeasca', 'pret': 4, 'locatie': 'cuptor'},
                   {'id': '3', 'nume': 'chifla', 'descriere': 'greceasca', 'pret': 6, 'locatie': 'raft'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '2', 'nume': 'bagheta', 'descriere': 'frantuzeasca', 'pret': 4, 'locatie': 'cuptor'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert (lista) == []

    undoList.append(lista)
    redoList.clear()

    lista = adaugaPaine("1", "franzela", "italiana", 5, "raft", lista)

    undoList.append(lista)
    redoList.clear()

    lista = adaugaPaine("2", "bagheta", "frantuzeasca", 4, "cuptor", lista)

    undoList.append(lista)
    redoList.clear()

    lista = adaugaPaine("3", "chifla", "greceasca", 6, "raft", lista)

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '2', 'nume': 'bagheta', 'descriere': 'frantuzeasca', 'pret': 4, 'locatie': 'cuptor'},
                   {'id': '3', 'nume': 'chifla', 'descriere': 'greceasca', 'pret': 6, 'locatie': 'raft'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '2', 'nume': 'bagheta', 'descriere': 'frantuzeasca', 'pret': 4, 'locatie': 'cuptor'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '2', 'nume': 'bagheta', 'descriere': 'frantuzeasca', 'pret': 4, 'locatie': 'cuptor'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '2', 'nume': 'bagheta', 'descriere': 'frantuzeasca', 'pret': 4, 'locatie': 'cuptor'},
                       {'id': '3', 'nume': 'chifla', 'descriere': 'greceasca', 'pret': 6, 'locatie': 'raft'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '2', 'nume': 'bagheta', 'descriere': 'frantuzeasca', 'pret': 4, 'locatie': 'cuptor'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'}]

    undoList.append(lista)
    redoList.clear()
    lista=adaugaPaine("4","paine alba","romanesca",7,"cuptor", lista)

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '4', 'nume': 'paine alba', 'descriere': 'romaneasca', 'pret': 7, 'locatie': 'cuptor'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert (lista) == []

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '4', 'nume': 'paine alba', 'descriere': 'romaneasca', 'pret': 7, 'locatie': 'cuptor'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert (lista) == [{'id': '1', 'nume': 'franzela', 'descriere': 'italiana', 'pret': 5, 'locatie': 'raft'},
                   {'id': '4', 'nume': 'paine alba', 'descriere': 'romaneasca', 'pret': 7, 'locatie': 'cuptor'}]