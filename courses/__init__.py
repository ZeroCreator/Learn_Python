# __init.py__ - инициализатор пакетов


#import courses.python
#from courses.python import get_python # абсолютный импорт


from .python import get_python # относительный импорт
from . import html, java, php, python
from .php import *
from .doc import *


NAME = "package courses"