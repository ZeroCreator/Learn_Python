# Classmethod and staticmethod.
'''
class Example:

    def hello():
        print("hello")
        # Можем вызвать от класса, но не можем вызывать от экземпляоа класса (instance)

    def instance_hello(self):
        print(f"instance_hello {self}")
        # Можем вызвать от экземпляоа класса (instance), но не можем вызывать от класса

Example.hello
Example.hello()

p = Example()
print(p.hello) # Можно вызвать от класса
# print(p.hello()) # Нельзя вызвать от экземпляра: TypeError: hello() takes 0 positional arguments but 1 was given

q = Example()
q.instance_hello()
print(q)
# Example.instance_hello() # TypeError: instance_hello() missing 1 required positional argument: 'self'
'''
# декоратор staticmethod - не привязывается ни к клссу, ни к экземпляру класса, поэтому его можно
# вызвать обоими способами
print("декоратор staticmethod")
class Example:
    def hello():
        print("hello")

    def instance_hello(self):
        print(f"instance_hello {self}")

    @staticmethod
    def static_hello():
        print("static_hello")

Example.static_hello()
y = Example()
y.static_hello()

# декоратор classcmethod - когда нужна обработка не экземплятор класса, а целого класса.
print("декоратор classcmethod")

class Example:
    def hello():
        print("hello")

    def instance_hello(self):
        print(f"instance_hello {self}")

    @staticmethod
    def static_hello():
        print("static_hello")

    @classmethod
    def class_hello(cls):
        print(f"instance_hello {cls}")

c = Example.class_hello()
print(c)

a = Example()
g = a.class_hello()
print(g)

print(a.__class__)