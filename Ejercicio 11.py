dinero_inicial = float(input("Introduzca el dinero depositado inicialmente"))
interés_primer_año = dinero_inicial * 0.04
dinero_primer_año = dinero_inicial - interés_primer_año
print("El dinero del tercer año es", round(dinero_primer_año))
interés_segundo_año = dinero_primer_año * 0.04
dinero_segundo_año = dinero_primer_año - interés_segundo_año
print("El dinero del tercer año es", round(dinero_segundo_año))
interés_tercer_año = dinero_segundo_año * 0.04
dinero_tercer_año = dinero_segundo_año - interés_tercer_año
print("El dinero del tercer año es", round(dinero_tercer_año))