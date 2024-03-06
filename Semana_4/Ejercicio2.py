from collections import deque
C=int(input())
for _ in range(C):
    f = deque(map(int,input().split()))
    while True:
        if len(f)>=2:
            if (f[-1]+f[-2])%2==0:
                f.append((f.pop()+f.pop())//2)
            else:
                print(len(f),f[-1])
                break
        else:
            print(1,f[-1])
            break