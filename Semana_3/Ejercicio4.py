from bisect import bisect_left
k=int(input())
postes=tuple(sorted(map(int,input().split())))
P=int(input())
for _ in range(P):
    pareja=tuple(map(int,input().split()))
    print(abs(bisect_left(postes,pareja[0])-bisect_left(postes,pareja[1])), "kms")