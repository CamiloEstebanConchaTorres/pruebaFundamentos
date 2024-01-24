
Voltaje1 = int(input("ingrese el valor del primer voltaje \n"))
Voltaje2 = int(input("ingrese el valor del segundo voltaje \n"))
Voltaje3 = int(input("ingrese el valor del tercer voltaje \n"))
Promedio = (Voltaje1 + Voltaje2 + Voltaje3 ) / 3
if Promedio < 115:
    print(f"{Promedio} = VOLTAJE CORRECTO")
else:
    if (Promedio >= 115) and (Promedio < 220):
        print(f"{Promedio} = ALTO VOLTAJE") 
    else:
        if Promedio >= 220:
           print(f"{Promedio} = PELIGRO")