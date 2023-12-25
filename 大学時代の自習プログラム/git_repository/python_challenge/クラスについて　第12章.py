import math
#1
class Apple:
    def __init__(self,w,c,s,q):
        self.weight=w
        self.color=c
        self.size=s
        self.quority=q
app=Apple(100,"blue","big","beautiful")
print(app.weight,app.color,app.size,app.quority)
#2
class Circle:
    def area(self,r):
        return math.pi*(r**2)
print(Circle.area(Circle,2))
#↑のareaメソッド内でselfでなくCircleを使うのはprintの実行が当然ながらクラス定義
#文の外にあるため、Circleクラスを引数に取ることを明示する必要があるため
#また、オブジェクトの生成と同時にメソッドをかけているので。

#3
class Triangle:
    def area(self,h,w):
        return h*w/2
a=Triangle()
b=a.area(4,8)
print(b)
#↑はaがTriangleクラスのオブジェクトであることを明示しているのでareaの引数は省略
#できる
#4
class Hexagon:
    def calculate_perimeter(self,r):
        return r*6
print(Hexagon.calculate_perimeter(Hexagon,6))
    
        
    
    
