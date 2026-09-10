# Programa para calcular el IMC

print("============================")
print("      Calcular el IMC")
print("============================")

#====================================
# Definimos las variables que se usaran
#====================================
apellido_paterno = input("Ingresa tu apellido paterno: \n")
apellido_materno = input("Ingresa tu apellido materno: \n")
nombre = input("Ingresa tu(s) nombre(s): \n")
edad = int(input("Ingresa tu edad: \n"))
peso = float(input("Ingresa tu peso en kilogramos: \n"))
estatura = float(input("Ingresa tu estatura en metros: \n"))

#====================================
#   Formula para calcular el IMC
#====================================
imc = peso / (estatura **2) #<----Peso entre estatura al cuadrado

#====================================
# Imprimimos en pantalla la informacion y el resultado
#====================================
print("*****************************")
print("           Datos")
print("*****************************")
print("Nombre: ", apellido_materno, apellido_paterno, nombre)
print("\nPeso: ", peso)
print("\nEstaura: ", estatura)
print("\n============================")
print("   IMC: ",round(imc, 4))     #<------ Redondeamos a solo 4 decimales
print("============================")


