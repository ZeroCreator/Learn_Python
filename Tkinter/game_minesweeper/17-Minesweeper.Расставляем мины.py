#  Minesweeper in Python Tkinter
# Игра "Сапер" на Python, создаем игровое поле.
import tkinter as tk
from random import shuffle


class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number # нумеруем каждую кнопку для определения количества кнопок
        self.is_mine = False

    def __repr__(self):
        return f"MyButton {self.x} {self.y} {self.number} {self.is_mine}"


class MineSweeper:
    window = tk.Tk()
    ROW = 10
    COLUMN = 7
    MINES = 15

    def __init__(self):
        self.buttons = []
        count = 1 # счетчик для нумерации кнопок
        for i in range(MineSweeper.ROW):
            temp = []  # временный список
            for j in range(MineSweeper.COLUMN):
                btn = MyButton(MineSweeper.window, x=i, y=j, number=count)
                temp.append(btn)
                count += 1 # счетчик для нумерации кнопок
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMN):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        print(self.get_mines_places())
        MineSweeper.window.mainloop()


    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)


    # метод для вставки мин
    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        for row_btn in self.buttons:
           for btn in row_btn:
               if btn.number in index_mines:
                   btn.is_mine = True

    # метод для расположения бомб
    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.COLUMN * MineSweeper.ROW + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


game = MineSweeper()
game.start()









