from UI.Console import runMenu
from tests.testAll import runAllTests
from UI.Console2 import meniu

def main():
    lista=[]
    optiune=input("Alege o optiune:")
    if optiune=="1":
        runMenu(lista)
    elif optiune=="2":
        meniu(lista)
    runAllTests()
main()