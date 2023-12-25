#1
class Square:
    square_list=[]
    def __init__(self,number):
        self.square_list.append(self)
#2
        self.number=number
    def __repr__(self):
        return (str(self.number) +" by ")*3+str(self.number)
    #return "{}by{}by{}by{}".format(self.number,self.number,self.number,self.number)
    #の方が足し算を使うためにいちいちデータ型をstrに変える必要がなくて良い
a=Square(4)
print(Square.square_list)
print(a)

def whitch(one,two):
    if one is two :
        return True
    else:
        return False

b=a
print(whitch(a,b))
c=Square(4)
print(whitch(a,c))

print(Square.square_list)
