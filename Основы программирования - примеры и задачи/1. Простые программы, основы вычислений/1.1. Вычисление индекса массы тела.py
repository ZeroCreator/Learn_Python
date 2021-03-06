# 1.2 Задача. Вычисление индекса массы тела и его интерпретация
'''
Задача
Определить индекс массы тела человека по его росту и весу, а затем интерпретировать результат в соответствии с рекомендациями Всемирной Организации Здравоохранения:

Индекс массы тела	        Описание
меньше 18,5	            Недостаточная масса тела
18,5 - 24,99	        Нормальная масса тела
25 - 29,99	            Избыточная масса тела
больше или равно 30 	Ожирение
'''
# I этап. Неформальная постановка
'''
Входные данные: 
    Описание	                    Пример	            Недопустимые
                                                            значения
Имя пользователя	            Paul, Ольга, Артем	        -
Возраст (количество полных лет)	23, 45, 16	<10
Рост (м)	                    1.78, 1.65, 1.85	    0 < ИЛИ > 3
Вес (кг)	                    65, 58.7, 80.3, 75	    <0 ИЛИ > 500



Выходные данные: 
Описание	                    Пример
Индекс массы тела	        18.45, 24.12, 27.1
Заключение	                Недостаточная масса тела,
                            Нормальная масса тела,
                            Избыточная масса тела,
                            Ожирение
                            
Описание переменных:
Описание	                    Имя         Тип
Имя пользователя	            name	    string
Возраст (количество полных лет)	age	        int
Рост (м)	                    height	    float
Вес (кг)	                    weight	    float
Индекс массы тела	            bmi	        float
Заключение	                    description string

Используемые формулы:
Индекс массы тела рассчитывается по формуле:

bmi = {m\h^2}

где: bmi– индекс массы тела в кг/м²,
        m – масса тела в килограммах,
        h – рост в метрах.

Функциональные возможности:
Создаваемая программа должна:

спросить у пользователя его имя;
спросить у пользователя, сколько полных лет ему исполнилось;
вывести приветствие на экран;
спросить у пользователя его рост и вес;
вычислить индекс массы тела;
вывести индекс массы тела на экран;
вывести заключение по посчитанному индексу.                              
'''

# Переменные и типы
'''
Для хранения данных в программе используются переменные. Простыми словами, переменная – это некоторый объект, 
который имеет имя, значение и тип.
В нашем случае для описания имени человека будет использоваться переменная строкового типа (string), и она может принимать текстовые значения, заключенные в двойные или одинарные кавычки. Для обозначения возраста используется целая переменная (тип int), в которую можно занести любые целые значения. Для описания веса и роста будем использовать вещественный тип (float).   При вводе значений этого типа в качестве разделителя целой и дробной части используется только  точка.

Существует несколько правил для выбора имен переменных.

Имя должно состоять из букв, цифр и знаков подчеркивания, начинаться с буквы. Не может совпадать с ключевыми словами языка.
Python различает большие и маленькие буквы в имени (переменная x и X – разные переменные).
Имя переменной должно максимально точно соответствовать хранимым в ней данным.
Имена переменных могут состоять из нескольких слов, тогда они пишутся через подчеркивание  вот_так.
Примеры: age, user_age, weight, weight_person
'''