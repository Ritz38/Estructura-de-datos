N=int(input())
T=tuple(map(int,input().split()))
s=T[-1]
for i in range(-2,-N-1,-1):
    s+=T[i]
    print(s)
