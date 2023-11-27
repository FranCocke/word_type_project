from char_container import CharContainer
from sylabs_container import SylabsContainer
from functions import *

palabra = input("Introduce la plaba a separa por silabas: ")
silaba = SylabsContainer()
char_object = CharContainer(palabra)
print(char_object.word)
print(char_object.char_line)
print(char_object.type_line)
print(silaba.split(char_object))


print(f"tiene tile {has_tilde(silaba.split(char_object))}")
print(f"es aguda: {es_aguda(silaba.split(char_object))}")
print(f"es grave: {es_grave(silaba.split(char_object))}")
print(f"es esdrujula: {es_esdrujula(silaba.split(char_object))}")
print(f"es sobreesdrujula: {es_sobreesdrujula(silaba.split(char_object))}")

