from constants import *
from typing import Literal
TypesOfLetter = Literal["V", "v", "x", "s", "c"]

def char_type(char:str) -> TypesOfLetter:
    if char in V_FUERTE:
        return "V"  # strong vowel
    if char in V_DEBIL:
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


def has_tilde(silabas:list) -> bool:
    for silaba in silabas:
        for char in silaba:
            if char in V_TILDE:
                return True
    return False

def ends_with_mente(silabas:list) -> bool:
    return (silabas[-2] + silabas[-1]) == "mente"


def es_aguda(silabas:list) -> tuple[bool, str]:
    if has_tilde(silabas[-1]):
        return True, silabas[-1]
    if not has_tilde(silabas) and silabas[-1][-1] not in DEBIL_TERMINACION:
        return True, silabas[-1]
    return False, ""

def es_grave(silabas:list) -> tuple[bool, str]:
    if has_tilde(silabas[-2]):
        return True, silabas[-2]
    if not has_tilde(silabas) and silabas[-1][-1] in DEBIL_TERMINACION and not ends_with_mente(silabas):
        return True, silabas[-2]
    return False, ""

def es_esdrujula(silabas:list) -> tuple[bool, str]:
    if len(silabas) > 3:
        if has_tilde(silabas[-3]):
            return True, silabas[-3]
    if ends_with_mente(silabas) and not has_tilde(silabas) and es_aguda(silabas[:-2]):
        return True, silabas[-3]
    return False, ""

def es_sobreesdrujula(silabas:list) -> tuple[bool, str]:
    if len(silabas) > 3:
        if has_tilde(silabas[-4]):
            return True, silabas[-4]
    if len(silabas) > 4:
        if has_tilde(silabas[-5]):
            return True, silabas[-5]

    if ends_with_mente(silabas) and not has_tilde(silabas) and es_grave(silabas[:-2]):
        return True, silabas[-5]

    return False, ""
