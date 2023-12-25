def getTotalX(a, b):
    # Write your code here
    list1=[]
    List=[]
    count=[]
    def kouyakusuu(num,list1,list2):
        for j in list1:
            if num%j==0:
                continue
            else:
                return
        list2.append(num)
    def koubaisuu(num,list1,list2):
        for j in list1:
            if j%num==0:
                continue
            else:
                return
        list2.append(num)
            
            
                

    for i in range(a[-1],b[0]+1):
        if i%max(a)==0:
            list1.append(i)
    
    for i in list1:
        kouyakusuu(i,a,List)
    for i in List:
        koubaisuu(i,b,count)
    return len(count)
a=[2,4]
b=[16,32,64]
print(getTotalX(a,b))
