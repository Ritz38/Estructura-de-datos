I = set()
D = set()
C = set()
while True:
    entrada = input().split()
    if entrada[0]=="#":break
    
    entrada[0] = int(entrada[0])
    
    if entrada[1] == "pdi":
        if entrada[0] in I:
            continue
        else:
            I.add(entrada[0])
    
    elif entrada[1] == "pdd":
        if entrada[0] in D:
            continue
        else:
            D.add(entrada[0])
            
    elif entrada[1] == "pdc":
        if entrada[0] in C:
            continue
        else:
            C.add(entrada[0])
            
print((len(I - (D | C)) + len(D - (I | C)) + len(C - (I | D))),(len((I & D) - C) + len((I & C) - D) + len((D & C) - I)),len(I&D&C))