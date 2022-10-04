#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
#Después debe mostrar por pantalla la paga que le corresponde.


print("¿Cuantas horas lleva trabajadas?")
horas = float(input())
print("¿Cuanto cobra por hora?")
cobro = float(input())
dinero = horas * cobro
print ("Usted va a cobrar", dinero, "€")