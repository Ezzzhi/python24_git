"""
Реализовать свой вариант блокнота с возможностью:
- создать новый файл
- открыть существующий
- удалить существующий
- редактировать
- плюс меню с разделами об авторах и справка
"""

import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog as fd
import os

class File:
    def __init__(self, path, name, data):
        self.path = path
        self.name = name
        self.data = data

    def add(self):
        pass

# кнопка Открыть


window = tk.Tk()

window.title('Блокнот')
window.geometry("500x600")
txt = scrolledtext.ScrolledText(window)
txt.grid(column=0, row=0)
# txt.insert(0, 'Текстовое поле')
window.resizable(True, True)
batton_add = tk.Button(window, text="+", command=fd.askopenfilename)
# file = fd.askopenfilename() - открывает окно проводника
batton_add.place(x=50, y=150, width=50)

number1_entry = tk.Entry(window, width=50)
number1_entry.place(x=0, y=0)
# number1 = tk.Label(window, text='Введите первое число:')
# number1.place(x=60, y=20)
# number2_entry = tk.Entry(window, width= 30)
# number2_entry.place(x=60, y=100)
# number2 = tk.Label(window, text='Введите второе число:')
# number2.place(x=60, y=70)
# ans_entry = tk.Entry(window, width= 30)
# ans_entry.place(x=60, y=230)
# ans = tk.Label(window, text='Ответ:')
# ans.place(x=60, y=200)

window.mainloop()