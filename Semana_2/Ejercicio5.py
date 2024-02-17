C=int(input()) #C=2
for i in range(C):
    X=tuple(map(int,input().split()))
    Y=tuple(map(int,input().split()))
    integrantes=()
    for j in range(X[0]):
        integrantes+=(sum(Y[j::X[0]]),)
    print(max(integrantes)-min(integrantes))