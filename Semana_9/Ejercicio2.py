habitantes = set()
muertos = set()
while True:
    entrada = input().split()
    
    if entrada[0] == "E": break
    
    entrada[1] = int(entrada[1])
    
    if entrada [0] == "B":
        if entrada[1] in habitantes or entrada[1] in muertos: 
            continue
        else: 
            habitantes.add(entrada[1])
    
    elif entrada [0] == "D":
        if entrada[1] in habitantes:
            habitantes.remove(entrada[1])
            muertos.add(entrada[1])
        else: continue
        
    else:
        if entrada[1] in muertos:
            muertos.remove(entrada[1])
            habitantes.add(entrada[1])
        else:
            continue
        
        

print(len(habitantes))