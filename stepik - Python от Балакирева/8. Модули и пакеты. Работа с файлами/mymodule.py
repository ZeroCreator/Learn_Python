#import math

from math import pi, ceil

NAME = "mymodule"


def floor(x):
    print("функция floor из модуля mymodule")
    return x


#print(__name__)
print(NAME)

if __name__ == "__main__":
    for i in range(5):
        print(NAME)