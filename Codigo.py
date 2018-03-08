import random

print("Hola, en qué numero estoy pensando?")
a = random.randint(1,10)
d = False
b = 3
while d == False:
    c = int(input(""))
    if c == a:
        d = True
        print("ganaste")
    else:
        b += -1
        if b == 0:
            print("Perdiste, el numero correcto era ",a)
            break
        if c < a:
            print("Es mayor,te quedan ", b, " intentos")
        else:
            print("Es menor,te quedan ", b, " intentos")

