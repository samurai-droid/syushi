def birthday(s, d, m):
    # Write your code here
    list1=[]
    count=0
    for i in range(len(s)-m+1):
        list1.append(s[i:i+m])
    for i in list1:
        if sum(i)==d:
            count+=1
    return count