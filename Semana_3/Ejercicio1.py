from bisect import bisect_left
N=int(input())
T=tuple(map(int,input().split()))
M=int(input())
B=tuple(map(int,input().split()))
s=0
for i in B:
    j = bisect_left(T,i)
    if j!=N and T[j]==i:
        s+=j+1
print(s)