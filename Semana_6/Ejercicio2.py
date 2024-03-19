import heapq
A=[]
B=[]
C=[]
a=0
b=0
c=0
while True:
    x=input().split()
    if x[0]=="fin": break
    if x[0]=="menores":
        if not A and not B and not C: continue
        elif not A and not B and c:
            c += 1
        elif not A and B and not C:
            b += 1
        elif A and not B and not C:
            a += 1
        elif not A:
            if B[0]<C[0]:
                b += 1
            elif B[0]==C[0]:
                b +=1
                c +=1
            else:
                c +=1
        elif not B:
            if A[0]<C[0]:
                a += 1
            elif A[0]==C[0]:
                a +=1
                c +=1
            else:
                c +=1
        elif not C:
            if B[0]<A[0]:
                b += 1
            elif B[0]==A[0]:
                b +=1
                a +=1
            else:
                a +=1
        else:
            r = min(A[0],B[0],C[0])
            if A[0] == r:
                a += 1
            if B[0] == r:
                b += 1
            if C[0] == r:
                c += 1
        if A:
            heapq.heappop(A)
        if B:
            heapq.heappop(B)
        if C:
            heapq.heappop(C)
    else:
        if x[0]=="A": heapq.heappush(A,int(x[1]))
        elif x[0]=="B": heapq.heappush(B,int(x[1]))
        else: heapq.heappush(C,int(x[1]))
print("Equipo A:",a)
print("Equipo B:",b)
print("Equipo C:",c)