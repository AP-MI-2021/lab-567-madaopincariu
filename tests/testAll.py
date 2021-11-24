from tests.testCRUD import testAdaugaPaine, testStergePaine, testModificaPaine
from tests.testDomain import testPaine
from tests.testFuctionalitati import testMutare, testSumaPretPerLocatie, testOrdonareDupaPret, testConcatenare, \
    testPretMaxPerLocatie
from tests.testUndoRedo import test_undo_redo


def runAllTests():
    testPaine()
    testAdaugaPaine()
    testStergePaine()
    testModificaPaine()
    testPretMaxPerLocatie()
    testConcatenare()
    testOrdonareDupaPret()
    testSumaPretPerLocatie()
    testMutare()
    test_undo_redo()
