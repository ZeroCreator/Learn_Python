# Minesweeper in Python Tkinter
# Игра "Сапер" на Python, создаем игровое поле.
import tkinter as tk

window = tk.Tk()

ROW = 5
COLUMN = 7

buttons = []
for i in range(ROW):
    temp = []   # временный список
    for j in range(COLUMN):
        btn = tk.Button(window, width=3, font='Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)

# for row_btn in buttons:
#     print(row_btn)

for i in range(ROW):
    for j in range(COLUMN):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)

window.mainloop()