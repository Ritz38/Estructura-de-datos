N= int(input())
SO=tuple(map(int,input().split(", ")))
LAR=tuple(map(int,input().split(", ")))
IS=tuple(map(int,input().split(", ")))
so=0
lar=0
iss=0
for i in range(N):
    if (SO[i]+LAR[i]+IS[i])%2==0:
        if SO[i]%2==0: so+=1
        if LAR[i]%2==0: lar+=1
        if IS[i]%2==0: iss+=1


    else:
        if SO[i]%2!=0: so+=1
        if LAR[i]%2!=0: lar+=1
        if IS[i]%2!=0: iss+=1
print(f"SO:{so}, LAR:{lar}, IS:{iss}")



