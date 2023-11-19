class char_line:
    def __init__(self, word):
        self.word = word
        self.V_STRONG = ["a", "á", "e", "é", "o", "ó", "í", "ú"]
        self.V_WEEK = ["i", "u", "ü"]

        # define una lista de tuplas con la letra y el tipo de letra, sea
        # a, á, e, é, o, ó, i, ú: vocal fuerte
        # i, u, ü: vocal debil
        # x: x
        # s: s
        # consonante
        self.char_line = [(char, self.char_type(char)) for char in word]

        # escribe la plabara segun el tipo de las letras
        self.type_line = "".join(chartype for _, chartype in self.char_line)

    def char_type(self, char):
        if char in self.V_STRONG:
            return "V"  # strong vowel
        if char in self.V_WEEK:
            return "v"  # week vowel
        if char == "x":
            return "x"
        if char == "s":
            return "s"
        else:
            return "c"

    # devuelve la posisicion si se encuentra una rule de separado
    def find(self, finder):
        return self.type_line.find(finder)

    # devuelve dos clases char_line desde la posicion 0 hasta
    # la posicion en que se encuentra la rule para separar
    # más la posicion en que se debe separar segun la rule
    # y la otra parte es el resto
    def split(self, pos, where):
        return (
            char_line(self.word[0 : pos + where]),
            char_line(self.word[pos + where :]),
        )

    # si se encuentra un split_point por la function find del objeto
    # etonces se returna una tupla con dos objetos char_line
    # si no se encuentra se devuelve false como segundo value de la tupla
    # que sirve para validar si se debe ejecutar una vuelta del ciclo en split de silabizer
    def split_by(self, finder, where):
        split_point = self.find(finder)
        if split_point != -1:
            chl1, chl2 = self.split(split_point, where)
            return chl1, chl2
        return self, False

    def __str__(self):
        return self.word

    def __repr__(self):
        return repr(self.word)


class silabizer:
    def __init__(self):
        self.RULES = [
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

        self.SINGLE_RULES = ["c", "s", "x", "cs"]

    # itera por cada rule para separar y las envia como parametros a las funciones de char_line
    def split(self, chars):
        for split_rule, where in self.RULES:
            # obtiene char_line, char_line
            # o obtiene char_line, False
            first, second = chars.split_by(split_rule, where)

            # si second no es False se ejecuta
            if second:
                # saltar la iteracion sirve para no agregar al array palabras mal separadas.
                # es decir, si una separación se hace incorrectamente no se va a agregar al array
                # y se va a seguir buscando una regla que separe correctamente la plabara

                # si una de las dos parte es un single rule se salta la iteración
                if (
                    first.type_line in self.SINGLE_RULES
                    or second.type_line in self.SINGLE_RULES
                ):
                    continue

                # si la ultima letra de la primera parte es consonate
                # y la primera de la segunda parte es una l o una r
                # salta la iteración
                if first.type_line[-1] == "c" and second.word[0] in set(["l", "r"]):
                    continue

                # si la primera letra y la ultima son l se salta la iteración
                if first.word[-1] == "l" and second.word[-1] == "l":
                    continue

                # si la ultima y la primera letra son r se salta la iteración
                if first.word[-1] == "r" and second.word[-1] == "r":
                    continue

                # si la ultima letra es c y la primera es h se salta la iteración
                if first.word[-1] == "c" and second.word[-1] == "h":
                    continue

                # se hace la suma del array resultante cuando termina el bucle for
                # son las sumas de las silabas de la primera parte más las sumas de las silabas de la seguna
                return self.split(first) + self.split(second)
        return [chars]

    def __call__(self, word):
        return self.split(char_line(word))


palabra = input("Introduce la plaba a separa por silabas: ")
silaba = silabizer()
char_object = char_line(palabra)
print(char_object.char_line)
print(char_object.type_line)
print(silaba(palabra))
