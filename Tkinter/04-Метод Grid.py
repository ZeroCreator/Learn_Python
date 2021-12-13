# Размещение виджетов при помощи метода grid().
# С помощью таблицы.
import tkinter as tk

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("Мое первое графическое приложение")

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f"Hello {i} {j}").grid(row=i, column=j, stick="we")

# btn1 = tk.Button(win, text="hello 1")
# btn2 = tk.Button(win, text="hello 2")
# btn3 = tk.Button(win, text="hello 3")
# btn4 = tk.Button(win, text="hello world")
# btn5 = tk.Button(win, text="hello 5")
# btn6 = tk.Button(win, text="hello 6")
# btn7 = tk.Button(win, text="hello 7")
# btn8 = tk.Button(win, text="hello 8")
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, stick="w")
# btn3.grid(row=1, column=0, stick='we')
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1, stick="e")
# btn7.grid(row=3, column=0, columnspan=2, stick='we')
# btn8.grid(row=0, column=2, rowspan=4, stick='ns')


win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()