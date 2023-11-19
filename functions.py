from constants import *
from enum import Enum
from typing import Literal
TypesOfLetter = Literal["V", "v", "x", "s", "c"]

def char_type(char:str) -> TypesOfLetter:
    if char in V_STRONG:
        return "V"  # strong vowel
    if char in V_WEEK:
        return "v"  # week vowel
    if char == "x":
        return "x"
    if char == "s":
        return "s"
    else:
        return "c"


# devuelve la posisicion si se encuentra una rule de separado
def last_is_consontant(string:str) -> bool:
    return True if string[-1] == "c" else False

def is_one_of(word:str, position:int, letters:list) -> bool:
    return True if word[position] in letters else False
