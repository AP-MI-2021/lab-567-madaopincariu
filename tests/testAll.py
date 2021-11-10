from tests.testCRUD import testAdaugaPaine, testStergePaine, testModificaPaine
from tests.testDomain import testPaine
from tests.testFuctionalitati import testMutare, testSumaPretPerLocatie, testOrdonareDupaPret, testConcatenare, \
    testPretMaxPerLocatie

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
