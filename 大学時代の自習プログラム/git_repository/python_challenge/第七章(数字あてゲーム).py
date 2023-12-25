#1
list=["ウォーキングデッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for i in list:
    print(i)
#2
for i in range(25,51):
    print(i)
#3
for i,j in enumerate(list):
    print(i,j)
#4
def hit():
    answer=[3,5,10]
    print("数字あてゲーム")
    while True:
        a=input("0~10までの数字を入力してください。qで終了")
        try:
        
            if 0<=int(a)<=10 and int(a) in answer:
                print("正解")
            else:
                print("不正解")
        except ValueError:
            
            if a=="q":
                print("終了します")
                break
        
            else:
                print("※qで終了、または0~10までの数字を入力")

hit()
