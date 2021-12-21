#  Minesweeper in Python Tkinter
# Игра "Сапер" на Python, создаем класс MineSwepper.
import tkinter as tk


class MineSweeper:
    window = tk.Tk()
    ROW = 10
    COLUMN = 7

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROW):
            temp = []  # временный список
            for j in range(MineSweeper.COLUMN):
                btn = tk.Button(MineSweeper.window, width=3, font='Calibri 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMN):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.print_buttons()
        MineSweeper.window.mainloop()


    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)


game = MineSweeper()
game.start()









