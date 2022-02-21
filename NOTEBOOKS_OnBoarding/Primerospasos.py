print("Hola terminal ")

sum=1+2 #3
product=sum*2
print(product)
#Operadores de asignacion
x=2
x+=2
print(x)


#Las fechas 
# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola usando str
print("Today's date is: "+str(date.today()))

#Entrada del usuario 
print("Bienvenido al programa de bienvenida ")
name= input("Introduzca su nombre ")
print("Saludos"+ name)


#Trabajar con numeros 

first_number=3
second_number=4
print(int(first_number)+int(second_number))