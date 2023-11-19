from char_container import CharContainer
from sylabs_container import SylabsContainer
from functions import *

palabra = input("Introduce la plaba a separa por silabas: ")
silaba = SylabsContainer()
char_object = CharContainer(palabra)
print(char_object.char_line)
print(char_object.type_line)
print(silaba(palabra))
