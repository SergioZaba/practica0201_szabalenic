numero_de_barras_viejas = int(input("Escriba el numero de barras vendidas que no son del dia"))
precio_barra_normal = 3.49
descuento = 0.6
coste_final = (precio_barra_normal * descuento) * numero_de_barras_viejas
print("El precio habitual de una barra de pan es", precio_barra_normal)
print("El descuento que se hace por no ser fresca es", descuento)
print("El coste final es", coste_final)