def andProduct(a, b):
    # Write your code here
    def func(n):
            count=0
            while n//2!=0:
                n=n//2
                count+=1
            return count
    def binary(num):
        length=func(num)
        dic={2**i:0 for i in range(length+1)}
        while num!=0:
            dic[2**func(num)]+=1
            num-=2**func(num)
        return dic
    
    lists=[binary(i) for i in range(a,b+1)]
    Max=func(b)
    
    diction={2**i:0 for i in range(Max+1)}
    Sum=0
    for i in range(Max+1):
        for j in lists:
            if 2**i in j and j[2**i]==1:
                diction[2**i]+=1
        if diction[2**i]==len(lists):
            Sum+=2**i
    return Sum
print(andProduct(42,57))
