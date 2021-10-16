# Пакет (package) - это специальным образом организованный подкаталог
# с набором модулей, как правило, решающих сходные задачи.
import courses

courses.python.get_python()

print(dir(courses))

courses.get_php()

print(courses.python_doc.doc)