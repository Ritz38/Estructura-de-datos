num=[]
while True:
    x=input().split()
    if x[0]=="end": break
    if x[0]=="C": 
        if len(num)>0:num.pop()
        else:continue
    elif x[0]=="D": 
        e=int(x[1])
        if e>len(num): continue
        else: num =num[:-e:]
    elif x[0]=="M":
        y=int(x[1])
        z=int(x[2])
        l=len(num)
        if y>l or z>l: continue
        else: 
            s=""
            for i in num[y-1:z:]:
                s+=i
            print(s)
    else: num.append(x[0])