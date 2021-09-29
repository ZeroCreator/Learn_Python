# Замыкания в Python. Вложенные функции.
def say_name(name):
    def say_goodbye():
        print("Don't say me godbye, " + name + "!")

    say_goodbye()

say_name("Sergey")