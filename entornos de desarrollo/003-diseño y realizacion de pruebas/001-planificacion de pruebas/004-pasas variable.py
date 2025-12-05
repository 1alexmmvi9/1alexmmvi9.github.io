def division (dividendo,divisor):
    try:
        if divisor == 0:
            return True
        else:
            return dividendo/divisor
    except:
        return False
pasas = True
for i in range(0,100):
    for j in range (0,100):
        if division(i,j) == False:
            pasas = False
            print(i,j)

if pasas == True:
    print("Prueba superada")
else:
    print ("prueba no superada")
