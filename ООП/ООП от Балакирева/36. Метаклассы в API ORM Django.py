# Метаклассы в API ORM Django.
# Используется для связи объектов с записями базы данных
# Используются для реализации API ORM Django

# Логика формирования свойств вынесена в метакласс:
class Meta(type):
    def creat_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.creat_local_attrs

class Women(metaclass=Meta):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

# class Women:
#     class_attrs = {'title': 'заголовок', 'content': 'контент', 'photo': 'путь к фото'}
#     title = 'заголовок'
#     content = 'контент'
#     photo = 'путь к фото'
#
#     def __init__(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#                 self.__dict__[key] = value

w = Women()
print(w.__dict__)
