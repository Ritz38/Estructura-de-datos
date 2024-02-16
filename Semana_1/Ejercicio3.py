N=int(input())
Q=0
R=0
for i in range(N):
    x=int(input())
    if x>=0:
        Q+=x
    else:
        R+=x
print(f"positivos {Q}, negativos {R}")