#ejemplo 1
rta = "salida = "
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    rta = rta + str(i) + " , "

print(rta)


#ejemplo 2
rta = "salida = "
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("Voy a sacar 5 en calculo")
 
#ejemplo 3
rta = "salida = "
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    rta = rta + str(i) + " , "
print(rta)

#ejemplo 4
rta = "salida = "
for i in range(1,11):
    rta = rta + str(i) + " , "
    print(rta)
    
#ejemplo 5
rta = "salida = "
for i in "UIS NO ES UNO":
    rta = rta + str(i) + " , "
    print(rta)

#ejemplo 5
suma = 0
for i in range(1,11):
    suma = suma + i
    
print("La suma es " + str(suma))

#ejemplo 7
frase = int(input("Digite una frase: "))
vocales = "aeiouAEIOU" 
numero_vocales = 0
for i in frase:
    if i in vocales:
        numero_vocales = numero_vocales + 1
print(f"En la frase hay un numero de vocales de " + str(numero_vocales))





