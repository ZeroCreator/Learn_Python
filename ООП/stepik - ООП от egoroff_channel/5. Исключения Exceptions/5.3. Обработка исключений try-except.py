# Обработка исключений try-except.
# 1/0
# a + b
# int("hello")
s = 'hello'
d = {}
try:
    4 + 8
    # 1 + 'fda'
    # d['key']
    # s[6]
    # a + b
    # int("hello")
    # 1 / 0
    # a + b
    print("123")
except Exception:
    print('error')
# except ValueError:
#     print("error ValueError")
# except ZeroDivisionError:
#     print("error ZeroDivisionError")
# except NameError:
#     print("error NameError")
# except KeyError:
#     print("error KeyError")
# except LookupError:
#     print("error LookupError")
# finally:
#     print("end")
#
# f = open("123.txt")
# try:
#     execute(f)
# finally:
#     print('End')
#     f.close()

try:
    1 / 5
except (KeyError, IndexError):
    print("LookupError")
else:
    print("good") # выведется только если не будет исключений
finally:
    print("End") # выведется в любом случае
