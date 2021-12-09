# Виджет Button. Кнопка tkinter.

def say_hello():
    print('hello')

def add_label():
    label = tk.Label(win, text='new')
    label.pack()

def counter():
    global count
    count +=1
    btn4['text']=f'Счетчик: {count}'

count = 0

import tkinter as tk
win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Мое первое графическое приложение')

btn1 = tk.Button(win, text="Hello",
                 command=say_hello
                 )

btn2 = tk.Button(win, text="Add new label",
                 command=add_label
                 )

btn3 = tk.Button(win, text="Add new label lambda",
                 command=lambda: tk.Label(win, text='new lambda').pack()
                 )

btn4 = tk.Button(win, text=f"Счетчик: {count}",
                 command=counter,
                 activebackground='blue',
                 bg='red',
                 state=tk.NORMAL # переключатель
                 )
btn1.pack() # размещение кнопки на рабочем столе
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()