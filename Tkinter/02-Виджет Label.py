# Виджет Label. (Отображение текстовой информации).
import tkinter as tk

win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title("Мое первое графическое приложение")

# Первый виджет
label_1 = tk.Label(win, text="Hello\nworld!",
                   bg='red',
                   fg="white",
                   font=("Arial", 15, "bold"),
                   # расположение текста относительно углов
                   padx=20, # отступы от краев по х
                   pady=40, # отступы от краев по y
                   width=20, # количество знаков по ширине
                   height=10, # количество знаков по высоте
                   anchor='sw', # расположение текста (w - e, n - s, c - if center)
                   # границы
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT # выравнивание
                   )

label_1.pack() # расположить виджет на рабочем столе


win.mainloop()
