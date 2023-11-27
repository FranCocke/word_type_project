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
