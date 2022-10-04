cantidad = float(input("Introduzca la cantidad de dinero que desea invertir"))
interes = float(input("Introduzca el interés anual entre 0 y 1"))
anos = float(input("Introduzca los años de la inversión"))

capital_obtenido = cantidad + (cantidad * interes * anos)
print ("Su capital obtenido es", capital_obtenido)