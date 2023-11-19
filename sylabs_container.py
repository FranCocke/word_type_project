from char_container import CharContainer
from functions import *
class SylabsContainer:
    # itera por cada rule para separar y las envia como parametros a las funciones de char_line
    def split(self, chars:CharContainer) -> list[str]:
        for split_rule, where in RULES:
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
                    first.type_line in SINGLE_RULES
                    or second.type_line in SINGLE_RULES
                ):
                    continue

                # si la ultima letra de la primera parte es consonate
                # y la primera de la segunda parte es una l o una r
                # salta la iteración
                if last_is_consontant(first.type_line) and is_one_of(word=second.word, position=0, letters=['l', 'r']):
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
        return [chars.word]


    def __call__(self, word):
        return self.split(CharContainer(word))
