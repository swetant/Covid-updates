import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=''
    k=[]
    for i in a:
        if i==0:
            ans+='0'
        else:
            k.append(ans)
            ans=''
    k.append(ans)
    a1=[]
    for i in range(len(k)):
        a1.append(len(k[i]))
    t=max(a1)
    a1.remove(t)
    if t%2==0:
        print("No")
    else:
        for i in a1:
            if (i>(t//2)):
                print("No")
                break
        else:
            print('Yes')
