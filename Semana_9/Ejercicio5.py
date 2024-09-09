F = set()
G = set()

while True:
    entrada = input().split()
    entrada[0] = int(entrada[0])
    if entrada[0] == 0: break
    
    if entrada[1] == "F":
        F.add(entrada[0])
        
    elif entrada[1] == "G":
        G.add(entrada[0])
        
juntos = F&G

F = F-juntos
G = G-juntos

for i in juntos:
    if i%2==0:
        F.add(i)
    else:
        G.add(i)
        
print(len(F),len(G))
