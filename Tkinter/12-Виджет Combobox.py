# Виджет Combobox.
import tkinter as tk
from tkinter import ttk

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point {self.x} {self.y}"


def show_day():
    print(combo.get(), combo_int.get())
    # if combo_int.get() == 5:
    #     print('well') # не сработает, так как идет преобразование числа в строку

def set_day():
    combo.set('Friday')


weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
list_int = [1, 2, 3, 4, 5]

win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('Мое первое приложение')

combo = ttk.Combobox(win, values=weekDays)
combo_int = ttk.Combobox(win, values=list_int)
combo_point = ttk.Combobox(win, values=[Point(2, 5), Point(1, 1)])
ttk.Button(win, text='show_day', command=show_day).pack()
ttk.Button(win, text='set_day', command=set_day).pack()
# дефортное значение поля (по умолчанию)
combo.current(0)  # индекс кортежа значений
combo_int.current(4)
combo.pack()
combo_int.pack()
combo_point.pack()

win.mainloop()
