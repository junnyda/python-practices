from typing import overload


class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)
     @staticmethod
     @overload
    def diff(c,a,b):
        print("diff 3개짜리")
    @staticmethod
    @overload
    def printCount():
        print(2)
    
