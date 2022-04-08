# Функция open. Чтение данных из файла
# Относительные пути к файлу: "my_file.txt"  , "images/img.txt, "../ouy.txt", "../patent/prt.dat"
# Абсолютные пути к файлу: "d:\\app\\my_file.txt"   , "d:/app/my_file.txt"   , "d:/app/images/img.txt"
# "d:/out.txt", "d:/parent/prt.dat"
file = open("my_file.txt", encoding='utf-8')

#print(file.read())
print("print(file.read())")

print(file.read(4))
print(file.read(4)) # файловая позиция - начало чтения (#FEFF)
print(file.read(4)) # EOF (end Of File)

# Управление положением файловой позиции - метод file.seek(offset[,from_what])
print("Управление положением файловой позиции - метод file.seek(offset[,from_what])")
file.seek(0)
print(file.read(4))

# Возвращение текущей файловой позиции - метод file.tell()
print("Возвращение текущей файловой позиции (номер байта!!!) - метод file.tell()")
print(file.read(4))
pos = file.tell()
print(pos)

# Прочитать первую строку - метод readline()
print("Прочитать первую строку - метод readline()")
file.seek(0)
print(file.readline(), end='') # \n - конец строки
print(file.readline())

# Построчное чтение файла:
print("Построчное чтение файла:")
file.seek(0)
for line in file:
    print(line, end="")

print()
# Метод file.readlines() - список из строк
print("Метод file.readlines() - список из строк")
file.seek(0)

s = file.readlines()
print(s)

# Закрытие файла - метод file.close() - освобождаем память
print("Закрытие файла - метод file.close()")
file.close()