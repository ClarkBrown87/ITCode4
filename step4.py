"""
Ну в общем __str__ нужен в первую очередь для пользователя,
вывод какой то информации об объекте, принты там, str
"""

class MyClass:
    def __init__(self):
        print("MyClass::__init__()")

    def __str__(self):
        return "MyClass::__str__()"


user_obj = MyClass()
print(user_obj)
print(str(user_obj))
