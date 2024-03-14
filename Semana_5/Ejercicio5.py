M=int(input())
num=[]
c=0
while True:
    n=int(input())
    if n==0: break
    num.append(n)
    c+=1
    if c%M==0:
        num.sort()
        if c%2!=0:
            print(num[(c//2)])
        else:
            s=num[(c//2)-1]+num[c//2]
            if (s)%2==0:
                print(s//2)
            else:
                print(f"{num[(c//2)-1]+num[c//2]}/2")