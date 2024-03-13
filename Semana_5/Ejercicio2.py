c=int(input())
for _ in range(c):
    x=list(map(int,input().split()))
    l=list(range(1,x[0]+1))
    posicion=0
    cantidadJugadores=x[0]
    while cantidadJugadores>1:
        print(l)
        if posicion+(x[1]%cantidadJugadores)>cantidadJugadores:
            posicion=x[1]%cantidadJugadores-((cantidadJugadores+1)-posicion)
        else: posicion= posicion+(x[1]%cantidadJugadores)
        chao=l.pop(posicion-1)
        cantidadJugadores-=1
        x[1]=chao%cantidadJugadores
        if x[1]==0: x[1]=1
    print(l[0])
    