# from cal2 import Calculator
# from user import User

# cal1 =Calculator
# cal1.add(10)
# cal1.diff(5)
# print(f"cal1\t.{cal1.result}")

# cal2 = Calculator()
# cal2.add(10)
# cal2.diff(5)
# print(f"cal2\t.{cal2.result}")


# cal3 = Calculator()
# cal3.add(10)
# cal3.diff(5)
# print(f"cal3\t.{cal3.result}")





# from user import User


# def arer(a,b):
#     return a+b

# user1 = User(id="bit", password="1234")
# user1.printUser()
# user1.change_id("pppp")
# user1.printUser()


from animal import Animal
# from leg import Leg


# l = Leg("left", "park")
# print(l.side)
# print(l.name)
# l.setName("kim")
# print(l.name)


an = Animal()
print(an.name)
an.__setattr__("name", "?")

print(an.__dict__)

from cat import Cat
from dog import Dog

cat = Cat()
cat.printSound()
print(cat.name)


dog = Dog()
dog.printSound()
print(cat.name)