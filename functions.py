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

def ends_with_ts(silabas:list) -> bool:
    return silabas[-1][-1:-3] == "ts"

def ends_with_mente(silabas:list) -> bool:
    return (silabas[-2] + silabas[-1]) == "mente"


def es_aguda(silabas:list) -> bool:
    for char in silabas[-1]:
        if char in V_TILDE:
            return True
    if not has_tilde(silabas) and silabas[-1][-1] not in DEBIL_TERMINACION:
        return True
    return False

def es_grave(silabas:list) -> bool:
    for char in silabas[-2]:
        if char in V_TILDE:
            return True
    if not has_tilde(silabas) and silabas[-1][-1] in DEBIL_TERMINACION and not ends_with_mente(silabas):
        return True
    return False

def es_esdrujula(silabas:list) -> bool:
    if len(silabas) > 3:
        for letra in silabas[-3]:
            if letra in V_TILDE:
                return True
    if ends_with_mente(silabas) and not has_tilde(silabas) and es_aguda(silabas[:-2]):
        return True
    return False

def es_sobreesdrujula(silabas:list) -> bool:
    if len(silabas) > 3:
        for letra in silabas[-4]:
            if letra in V_TILDE:
                return True
    if len(silabas) > 4:
        for letra in silabas[-5]:
            if letra in V_TILDE:
                return True

    if ends_with_mente(silabas) and not has_tilde(silabas) and es_grave(silabas[:-2]):
        return True
    return False
