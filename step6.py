"""Вообще миксины создаются, чтобы повторно использовать функции во множестве классов
Они не должны создавать объект и не должны иметь своего состояния
"""


class Run:
    def run(self):
        print("Run::run")

class Eat:
    def eat(self):
        print("Eat::eat")


class Human(Run, Eat):
    def __init__(self):
        print("Human::__init__")

h = Human()
h.run()
h.eat()
