def division (dividendo,divisor):
    try:
        if divisor == 0:
            return True
        else:
            return True
    except:
        return False
pasas = True
for i in range(-10,10,1):
    for j in range (-10,10,1):
        if division(i,j) == False:
            pasas = False
            print(i,j)

if pasas == True:
    print("Prueba superada")
else:
    print ("prueba no superada")
