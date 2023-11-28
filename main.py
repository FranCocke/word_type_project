from word_container import WordContainer

palabra = input("Ingresa la palabra que quieres clasificar: ")

word = WordContainer(palabra)

print(f"""La palabra {word.word}
tiene las silabas: {word.silabas}
es una palabra: {word.word_type}
y su silaba tónica es: {word.silaba_tonica}""")
