from sylabs_container import SylabsContainer
from functions import *


class WordContainer:
    def __init__(self, word: str) -> None:
        self.word = word
        self.silabs_container = SylabsContainer()
        self.silabas = self.silabs_container(word)
        self.get_type()

    def get_type(self) -> None:
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
        
        # si la palabra solamente tiene una silabra (nexos, preposiciones)
        # se le asigna el tipo aguda y la silaba tónica es la palabra misma
        self.word_type = "aguda"
        self.silaba_tonica = self.word

    @staticmethod
    def sanitize_sentence(sentence: str) -> list:
        words = sentence.split(" ")
        sanitized_words = list()
        for word in words:
            for char in word:
                if char in set([",", ".", ":", ";"]):
                    word = word[:word.find(char)] + word[word.find(char) + 1:]
            sanitized_words.append(word.lower())
        return sanitized_words
