n=[]
while True:
    x=list(input().split())
    if x[0]=="E": break
    x[1]= int(x[1])
    s=0
    
    if x[0]=="A": n.append(x[1])
    else:
        for i in n:
            if i%x[1]==0: s+=i
        print(s)