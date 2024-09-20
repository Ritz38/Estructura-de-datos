traductor = {}
for _ in range(int(input())):
    entrada = input().split()
    traductor[entrada[0]]=entrada[1]
    
while True:
    entrada2 = input()
    if entrada2 == "#": break
    
    if entrada2 in traductor:
        print(traductor[entrada2])
    else: 
        print("Entrada no encontrada")