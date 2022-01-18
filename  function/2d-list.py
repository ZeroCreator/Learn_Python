# обход вокруг позиции в двумерном списке
x = 5
y = 5
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        print(x + dx, y + dy)

# обход позиции вверх, вниз, вправо, влево
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        if abs(dx-dy) == 1:
            print(x + dx, y + dy)