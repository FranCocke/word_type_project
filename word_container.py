from sylabs_container import SylabsContainer
from char_container import CharContainer
from functions import *
class WordContainer():
    def __init__(self, word:str) -> None:
        self.word = word
        self.silabs_container = SylabsContainer()
        self.silabas = self.silabs_container(word)
        self.get_type()

    def get_type(self):
        word_type = es_aguda(self.silabas)
        if word_type[0]:
            self.word_type = "aguda"
            self.silaba_tonica = word_type[1]
            return

        word_type = es_grave(self.silabas)
        if word_type[0]:
            self.word_type = "grave"
            self.silaba_tonica = word_type[1]
            return

        word_type = es_esdrujula(self.silabas)
        if word_type[0]:
            self.word_type = "esdrújula"
            self.silaba_tonica = word_type[1]
            return

        word_type = es_sobreesdrujula(self.silabas)
        if word_type[0]:
            self.word_type = "sobreesdrújula"
            self.silaba_tonica = word_type[1]
            return
