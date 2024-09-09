robots = set(range(1,int(input())+1))

while True:
    entrada = input().split()
    if entrada[0]=="#": break
    if entrada[0]=="new":
        entrada[1] = int(entrada[1])
        entrada[2] = int(entrada[2])
        nuevo = entrada[1] + entrada[2]
        while True:
            if nuevo in robots: nuevo+=1
            else: break
        robots.add(nuevo)
        
    elif entrada[0] == "search":
        entrada[1] = int(entrada[1])
        if entrada[1] in robots:
            print("existe")
        else:
            print("no existe")
