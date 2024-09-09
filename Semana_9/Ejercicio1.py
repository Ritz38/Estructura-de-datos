V = set()
F = set()
Juntos = set()
while True:
    A = input().split()
    if A[0] =="#": break
    if A[0] == "V" and not (int(A[1]) in V):
        V.add(int(A[1]))
    elif A[0] =="F" and not (int(A[1]) in F):
        F.add(int(A[1]))

print(len(F),len(V),len(Juntos))