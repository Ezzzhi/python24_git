import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    ans_entry.delete(0, 'end')
    ans_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    if num2 == 0:
        insert_values('Error!')
    else:
        res = num1 / num2
        insert_values(res)


window = tk.Tk()

window.title('Калькулятор')
window.geometry("300x300")
window.resizable(False, False)
batton_add = tk.Button(window, text="+", command=add)
batton_add.place(x=50, y=150, width=50)
batton_sub = tk.Button(window, text="-", command=sub)
batton_sub.place(x=100, y=150, width=50)
batton_mul = tk.Button(window, text="*", command=mul)
batton_mul.place(x=150, y=150, width=50)
batton_div = tk.Button(window, text="/", command=div)
batton_div.place(x=200, y=150, width=50)

number1_entry = tk.Entry(window, width= 30)
number1_entry.place(x=60, y=50)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=60, y=20)
number2_entry = tk.Entry(window, width= 30)
number2_entry.place(x=60, y=100)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=60, y=70)
ans_entry = tk.Entry(window, width= 30)
ans_entry.place(x=60, y=230)
ans = tk.Label(window, text='Ответ:')
ans.place(x=60, y=200)

window.mainloop()