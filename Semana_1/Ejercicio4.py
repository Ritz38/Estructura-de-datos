N=int(input())
if N%2==0 or N%3==0 or N%5==0 or N%7==0:
    if N%2==0:
        print("es multiplo de 2")
    elif N%3==0:
        print("es multiplo de 3")
    elif N%5==0:
        print("es multiplo de 5")
    else:
        print("es multiplo de 7")
else:
    print("no es multiplo de ninguno de los primeros cuatro primos")