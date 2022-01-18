# Minesweeper in Python Tkinter
# Игра "Сапер" на Python, Обход в ширину.
import tkinter as tk
from random import shuffle

# online color picker
colors = {
    0: 'white',
    1: '#2403ff',
    2: '#2db504',
    3: '#8300f5',
    4: '#ff9203',
    5: '#81ff03',
    6: '#02f7f3',
    7: '#fc03ca',
    8: '#f7f702',
}


class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number  # нумеруем каждую кнопку для определения количества кнопок
        self.is_mine = False
        self.count_bomb = 0  # счетчик мин
        self.is_open = False # открывали эту кнопку или нет

    def __repr__(self):
        return f"MyButton {self.x} {self.y} {self.number} {self.is_mine}"


class MineSweeper:
    window = tk.Tk()
    ROW = 10
    COLUMNS = 7
    MINES = 15

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROW + 2):
            temp = []  # временный список
            for j in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    # функция для обработки кнопок
    def click(self, clicked_button: MyButton):
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state='disabled')  # выключение повторного нажатия кнопки
        clicked_button.config(relief=tk.SUNKEN) # эффект нажатия кнопки


    def breadth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:
            # обрабатываем нажатую кнопку используя метод графов
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disabled')  # выключение повторного нажатия кнопки
            cur_btn.config(relief=tk.SUNKEN)  # эффект нажатия кнопки

            if cur_btn.count_bomb == 0: # только для той кнопки, которая не имеет бомб
                x, y = cur_btn.x, cur_btn.y
                # обрабатываем соседей нажатой кнопки
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not abs(dx - dy) == 1:
                            continue

                        next_btn = self.buttons[x+dx][y+dy]
                        # добавляем кнопки в очередь (но только те, в которые еще не заходили)
                        if not next_btn.is_open and 1<=next_btn.x<=MineSweeper.ROW and \
                                1 <= next_btn.y <= MineSweeper.COLUMNS and next_btn not in queue:
                            queue.append(next_btn)

                    # отрисовка виджетов
    def create_widgets(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(MineSweeper.ROW + 2):
            for j in range(MineSweeper.COLUMNS + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        self.print_buttons()
        # self.open_all_buttons()
        print(self.get_mines_places())
        MineSweeper.window.mainloop()

    # вывод кнопок в консоль
    def print_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    # метод для вставки мин
    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

    # функция подсчета мин
    def count_mines_in_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                count_bobm = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i + row_dx][
                                j + col_dx]  # получаем всех возможных соседей для кнопки button
                            if neighbour.is_mine:
                                count_bobm += 1
                btn.count_bomb = count_bobm

    # метод для расположения мин
    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.COLUMNS * MineSweeper.ROW + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


game = MineSweeper()
game.start()
