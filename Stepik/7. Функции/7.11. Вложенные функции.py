# Вложенные функции.

g = 'gray' # Глобальная переменная
def colors(param='r'):
    y = 'yellow'
    g = 'green'
    def print_red():
        nonlocal y
        r = 'red'  # Локальнгая переменная
        print(r, y, g)
        y = 'was changed'

    def print_blue():
        b = 'blue' # Локальнгая переменная
        print(b, y, g)

    if param == 'r':
        print_red()
    elif param == 'b':
        print_blue()
    else:
        print('I do know this color')

colors(43)