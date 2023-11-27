from typing import Self
from functions import *

class CharContainer:
    def __init__(self, word:str):
        self.word = word

        # define una lista de tuplas con la letra y el tipo de letra, sea
        # a, á, e, é, o, ó, i, ú: V
        # i, u, ü: v
        # x: x
        # s: s
        # consonante: c
        self.char_line = [(char, char_type(char)) for char in word]

        # escribe la plabara segun el tipo de las letras
        self.type_line = "".join(chartype for _, chartype in self.char_line)


    # devuelve dos clases char_line desde la posicion 0 hasta
    # la posicion en que se encuentra la rule para separar
    # más la posicion en que se debe separar segun la rule
    # y la otra parte es el resto
    def split(self, pos:int, where:int) -> tuple[Self, Self]:
        return (
            CharContainer(self.word[0 : pos + where]),
            CharContainer(self.word[pos + where :]),
        )

    # si se encuentra un split_point por la function find del objeto
    # etonces se returna una tupla con dos objetos CharContainer
    # si no se encuentra se devuelve false como segundo value de la tupla
    # que sirve para validar si se debe ejecutar una vuelta del ciclo en split de silabizer
    def split_by(self, finder:str, where:int) -> tuple[Self, Self] | tuple[Self, bool]:
        split_point = self.type_line.find(finder)
        if split_point != -1:
            chl1, chl2 = self.split(split_point, where)
            return chl1, chl2
        return self, False
