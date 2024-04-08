
Voltaje1 = int(input("ingrese el valor del primer voltaje \n"))
Voltaje2 = int(input("ingrese el valor del segundo voltaje \n"))
Voltaje3 = int(input("ingrese el valor del tercer voltaje \n"))
Voltaje4 = int(input("ingrese el valor del cuarto voltaje \n"))
Voltaje5 = int(input("ingrese el valor del quinto voltaje \n"))
Promedio = (Voltaje1 + Voltaje2 + Voltaje3 + Voltaje4 + Voltaje5) / 5
if Promedio > 220:
     print(f"{Promedio} = ALTO VOLTAJE")
else:
     if Promedio < 220:
          print(f"{Promedio} = VOLTAJE CORRECTO") 
