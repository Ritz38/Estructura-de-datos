N=int(input())
print(N)
while N!=1:
    if N%2==0:
        N= N//2
        print(N)
    else:
        N= 3*N+1
        print(N)