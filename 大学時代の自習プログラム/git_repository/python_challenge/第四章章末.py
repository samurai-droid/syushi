#1
def exponentation(x):
    """return x**2
       param:x:int
       """
    return x**2
#2
def prin(str):
    print(str)
#3
def test(x,y,z,a=10,b=5):
    return x+y+z+a+b
#4
def ff(x):
    return x//2
def gg(x):
    return x*4
a=ff(4)
b=gg(a)
print(b)

#5
def floated(a):
    """入力された文字列型のデータを浮動小数型のデータに変換しようとする試み"""

    try:
        return float(a)
    except ValueError:
        print("InvalidInput")

c=exponentation(4)
print(c)
prin("のび太")
d=test(1,3,4)
print(d)
floated("のび太")
