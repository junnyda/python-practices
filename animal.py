
class Animal:
    def __init__(self) -> None:
        self.type = "sss"
        self.sound =""

    def setName(self,type):
        self.type = type

    def setName(self,sound):
        self.sound = sound

    def printSound(self):
        print(self.sound)


#  클래스 -> 하나의 물체를 만들기 위해 
#  상속 공통 코드 줄여줌 
