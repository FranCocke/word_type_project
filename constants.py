VOCALES = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
CONSONANTES = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
V_TILDE = ["á", "é", "ó", "í", "ú"]
V_NORMAL = ["a", "e", "i", "o", "u"]
V_FUERTE = ["a", "á", "e", "é", "o", "ó", "í", "ú"]
V_DEBIL = ["i", "u", "ü"]
DEBIL_TERMINACION = ["n", "s", "a", "e", "i", "o", "u", "ts"]

RULES = [
    ("VV", 1),
    ("cccc", 2),
    ("xcc", 1),
    ("ccx", 2),
    ("csc", 2),
    ("xc", 1),
    ("cc", 1),
    ("vcc", 2),
    ("Vcc", 2),
    ("sc", 1),
    ("cs", 1),
    ("Vc", 1),
    ("vc", 1),
    ("Vs", 1),
    ("vs", 1),
]

SINGLE_RULES = ["c", "s", "x", "cs"]

WORD_TYPES = {
    "SOBREESDRUJULA": "SOBREESDRÚJULA",
    "ESDRUJULA": "ESDRÚJULA",
    "GRAVE": "GRAVE",
    "AGUDA": "AGUDA",
}

RULES_EXPLANATIONS = {
    "ESDRUJULA": "Las palabras en las que su sílaba tónica es la antepenúltima",
    "SOBREESDRUJULA": "Las palabras en las que su sílaba tónica es la ante-antepenúltima",
    "GRAVE": "Las palabras en las que su sílaba tónica es la penúltima",
    "AGUDA": "Las palabras en las que su sílaba tónica es la útlima"
}
