#1
class Shape:
    def what_am_i(self):
        print("I am a"+str(self).split(" ")[0][9:])

import math
class Rectangle(Shape):
    def calculate_perimeter(self,h,w):
        return (h+w)*2
class Square(Shape):
    def __init__(self,r):
        self.haba=r
    def calculate_perimeter(self,r):
        return r*4
    def change_size(self,r):
        self.haba+=r
        
a=Rectangle()
print(a.calculate_perimeter(4,5))

#b=Square(4).change_size(2)←これはSquare(4)でinitメソッドを使ってるのでchangeが
#かかっている部分がメソッド（オブジェクトではなく）になってしまっているため不可?

b=Square(4)
b.change_size(-3)

print(b.calculate_perimeter(b.haba))

#2
#3
a.what_am_i()
b.what_am_i()
        
#4
class Horse:
    def __init__(self,rider):
        self.rider=rider
class Rider:
    def __init__(self,name):
        self.name=name
mike=Rider("mike")
horse=Horse(mike)
print(horse.rider.name)
