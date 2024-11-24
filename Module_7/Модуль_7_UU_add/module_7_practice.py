import tkinter as tk
import os
from tkinter import filedialog as fd

def file_select():
    filename = fd.askopenfilename(initialdir="/", title="Выберите файл",
                                  filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = 'Файл:\n' + filename
    os.startfile(filename)


window = tk.Tk() # создаем окно программы
window.title('Проводник') # назначаем название окна
window.geometry('350x350') # устанавливаем размер окна
window.resizable(False, False) # запрещаем пользователю менять размер окна

text = tk.Label(window, text='Файл: ', height=5, width=50, background='silver', foreground='blue')
text.grid(column=1, row=1)
button_select = tk.Button(window, text='Выберите файл',height=5, width=50,
                          background='silver', command=file_select)
button_select.grid(column=1, row=2)

window.mainloop() # постоянное обновление окна, последняя строка программы, зацикливающаяя ее