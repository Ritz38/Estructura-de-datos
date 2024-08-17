#Ordenamiento O(NlogN)
#Busqueda O(LogN) si esta ordenado
# 
# #bisect_left(lista, elemento)

        
cilindro = []

for _ in range(int(input())):
    entrada = list(map(int,input().split()))
    if entrada[0]==1:
        cilindro.append([entrada[1]*entrada[2],entrada[2]])
        
    else:
        suma=0
        i=0
        while True:
            
            if entrada[1]>cilindro[i][1]:
                suma+=cilindro[i][0]
                entrada[1]-=cilindro[i][1]
                cilindro.pop(0)
            else:
                suma=suma+cilindro[i][0]-(cilindro[i][0]//cilindro[i][1])*(cilindro[i][1]-entrada[1])
                if cilindro[i][1]==entrada[1]:
                    cilindro.pop(0)
                else:
                    cilindro[i][0]=(cilindro[i][0]//cilindro[i][1])*(cilindro[i][1]-entrada[1])
                    cilindro[i][1]= (cilindro[i][1]-entrada[1])
                print(suma)
                break

            

