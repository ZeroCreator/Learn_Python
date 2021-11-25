# Распространение исключений.
print("Исключения в функциях")
def third():
    print("start third")
    1/0
    # try:
    #     1/0
    # except ZeroDivisionError:
    #     print("handling")
    print("finish third")

def second():
    print("start second")
    third()
    print("finish second")

def first():
    print("start first")
    try:
        second()
    except ZeroDivisionError:
        print("handling first")
    print("finish first")

print("hello")
first()