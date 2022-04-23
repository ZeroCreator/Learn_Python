from lister import ListTree
from tkinter import Button


class MyButton(ListTree, Button):
    pass


B = MyButton(text="spam")
open("savetree.txt", "w").write(str(B))
print(B)