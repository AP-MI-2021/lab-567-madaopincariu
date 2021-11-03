from UI.Console import runMenu
from tests.testAll import runAllTests
from UI.Console2 import meniu

def main():
    runAllTests()
    lista=[]
    runMenu(lista)
    meniu()
main()