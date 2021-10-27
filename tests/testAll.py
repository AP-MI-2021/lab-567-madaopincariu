from tests.testCRUD import testAdaugaPaine, testStergePaine
from tests.testDomain import testPaine

def runAllTests():
    testPaine()
    testAdaugaPaine()
    testStergePaine()