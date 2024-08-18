"""https://www.codewars.com/kata/547274e24481cfc469000416/train/python"""
# 8 Kyu
# Basic subclasses - Adam and Eve

def God():
    return [Man(), Woman()]
class Human():
        pass

class Man(Human):
        
    def __init__(self):
        self.name = "Adam"
class Woman(Human):
        
    def __init(self):
        self.name = "Eve"