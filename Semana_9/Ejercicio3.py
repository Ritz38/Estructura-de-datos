E1 = set()
E2 = set()
E3 = set()
E4 = set()
E5 = set()

#E1
for _ in range(int(input())):
    E1.add(int(input()))
    
#E2
for _ in range(int(input())):
    E2.add(int(input()))

#E3
for _ in range(int(input())):
    E3.add(int(input()))
    
#E4
for _ in range(int(input())):
    E4.add(int(input()))
    
#E5
for _ in range(int(input())):
    E5.add(int(input()))
    
conjunto_mas_pequeno = min(E1, E2, E3, E4, E5, key=len)

cantidadE=0

for i in conjunto_mas_pequeno:
    if i in E1 and i in E2 and i in E3 and i in E4 and i in E5: cantidadE+=1
    
if cantidadE == 0: print("Nadie gana")
else: print(1000000//cantidadE)

