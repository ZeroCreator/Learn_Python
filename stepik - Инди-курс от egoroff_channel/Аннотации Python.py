# Аннотации Python.
"""
информативность исходного кода, и иметь возможность с помощью сторонних инструментов производить его анализ.
Одной из наиболее востребованных, в этом смысле, тем является контроль типов переменных
"""
from typing import List, Dict, Tuple, Optional, Any, Union

def add_numbers(a: int, b: Union[int, float, str] = None) -> int: # b: int | float | str
    return a + b


def list_upper(lst: List[str]):

    for elem in lst:
        print(elem.upper())

# Динамическая типизация:
first: int = 100
print(first)
#first = "hello"
#print(first)
second: int = 200
#print(add_numbers(first, second))
print(add_numbers('hello', 'world'))
print(add_numbers([1, 2, 3], [1, 4]))

print(add_numbers.__annotations__)

print(add_numbers(first))

d: Dict[str, int] = {"a": 100, "b": 200}

e: Any = 12
e = "fgjdhbf"

t: Optional[list] = [1, 2]



