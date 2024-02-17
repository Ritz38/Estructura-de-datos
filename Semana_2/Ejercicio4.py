N=int(input())
aa=tuple(input().split(", "))
r=""
for i in range(N//2):
    r+=aa[i]+aa[-i-1]
    if N%2!=0 and i==(N//2)-1:
        r+=aa[i+1]
        break
print(r)