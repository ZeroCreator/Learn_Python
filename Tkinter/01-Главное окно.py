# Введение в tkinter. Главное окно.
# Виджеты - элементы GUI, у которых есть определенные свойства.
# Программирование событийное - программа - обработчик событий.
import tkinter as tk

win = tk.Tk()
h = 500 # высота
w = 600 # ширина
# изменение иконки: iсons png fun
photo = tk.PhotoImage(file="fun.png") # изменение иконки: iсons png fun
win.iconphoto(False, photo)
# изменение цвета главного окна
# win.config(bg="red")
# либо с помощью RGB Color Wheel (https://www.colorspire.com/rgb-color-wheel/)
win.config(bg="#00EFFF")
win.title("Мое первое графическое приложение") # название программы
# win.geometry("500x600+100+200") # размеры окна + его расположение
win.geometry(f"{h}x{w}+100+200")
win.resizable(False, False) # Окно не растягивается/растягивается
win.minsize(300, 400) # минимальные рамки размеров
win.maxsize(300, 400) # максимальные рамки размеров

win.mainloop() # главный цикл - режим ожидания.

