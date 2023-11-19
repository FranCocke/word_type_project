V_STRONG = ["a", "á", "e", "é", "o", "ó", "í", "ú"]
V_WEEK = ["i", "u", "ü"]

def char_type(char):
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
