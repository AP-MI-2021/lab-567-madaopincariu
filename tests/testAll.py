from tests.testCRUD import testAdaugaPaine, testStergePaine, testModificaPaine
from tests.testDomain import testPaine

def runAllTests():
    testPaine()
    testAdaugaPaine()
    testStergePaine()
    testModificaPaine()