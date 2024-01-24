
base = float(input("ingrese la base del triangulo equilatero \n"))
altura = float(input("ingrese la altura del triangulo equilatero \n"))
area = base * altura

if area > 1000:
    print(f"el area es {area} - DATOS NO VALIDOS")
else:
    print(f"el area es {area}")