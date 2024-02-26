C=int(input())
for _ in range(C):
    N = tuple(sorted(map(int,input().split(", "))))
    A = N[:-1:]
    B = (N[-1],)
    while True:
        if abs(sum(B+(A[-1],))-sum(A[:-1:]))<=abs(sum(B)-sum(A)):
            B+=(A[-1],)
            A=A[:-1:]
        else:
            break
    print(abs(sum(B)-sum(A)))