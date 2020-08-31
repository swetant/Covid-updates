from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s1=set(a)
    a1=[]
    for i in s1:
        a1.append(a.count(i))
    a1.sort()
    c=Counter(a1)
    key=[]
    value=[]
    for i in c.keys():
        key.append(i)
    for i in c.values():
        value.append(i)
    b1=value.index(max(value))
    print(key[b1])

    #print(dict)
