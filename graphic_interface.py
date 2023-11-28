from word_container import WordContainer
import tkinter as tk
from typing import List


class UI:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("1080x720")
        self.words: List[WordContainer] = []
        self.create_main_objects()

        self.window.mainloop()

    def create_main_objects(self) -> None:
        self.entry_text = tk.Entry(self.window, width=50)
        self.entry_text.pack()
        self.accept_button = tk.Button(
            self.window, text="ACEPTAR", command=self.append_word
        )
        self.accept_button.pack()
        self.delete_button = tk.Button(
            self.window,
            text="BORRAR",
            command=self.reset_words,
            background="red",
            fg="#fff",
        )
        self.delete_button.pack()
        self.create_table()

    def create_table(self) -> None:
        self.table_frame = tk.Frame(self.window, width=500, height=500, bg="lightgrey")
        self.table_frame.pack()
        self.table_labels = tk.Frame(self.window, width=750, height=500, bg="lightgrey")
        self.table_labels.pack()
        title1 = tk.Label(
            self.table_frame,
            text="palabra",
            width=20,
            background="#000",
            font="#fff",
            fg="#fff",
        )
        title2 = tk.Label(
            self.table_frame,
            text="silabas",
            width=20,
            background="#000",
            font="#fff",
            fg="#fff",
        )
        title3 = tk.Label(
            self.table_frame,
            text="silaba tónica",
            width=20,
            background="#000",
            font="#fff",
            fg="#fff",
        )
        title4 = tk.Label(
            self.table_frame,
            text="tipo",
            width=20,
            background="#000",
            font="#fff",
            fg="#fff",
        )
        title1.grid(row=0, column=0)
        title2.grid(row=0, column=1)
        title3.grid(row=0, column=2)
        title4.grid(row=0, column=3)

    def append_word(self) -> None:
        words = WordContainer.sanitize_sentence(self.entry_text.get())
        for word in words:
            self.words.append(WordContainer(word))
        self.draw_words()
        self.entry_text.delete(0, tk.END)

    def draw_words(self) -> None:
        for index, word in enumerate(self.words):
            label_word = tk.Label(
                self.table_labels, text=word.word.capitalize(), width=30, fg="#000"
            )
            label_word.grid(row=index + 1, column=0)

            label_silabas = tk.Label(
                self.table_labels, text=word.silabas, width=30, fg="#000"
            )
            label_silabas.grid(row=index + 1, column=1)

            label_tonica = tk.Label(
                self.table_labels, text=word.silaba_tonica, width=30, fg="#000"
            )
            label_tonica.grid(row=index + 1, column=2)

            label_type = tk.Label(
                self.table_labels, text=word.word_type, width=30, fg="#000"
            )
            label_type.grid(row=index + 1, column=3)

    def reset_words(self) -> None:
        self.words.clear()
        for widget in self.table_labels.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()
        self.draw_words()
