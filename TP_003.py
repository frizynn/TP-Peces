# Se definen las constantes dadas en el problema
x0 = 237
y0 = 4980 # Es importante destacar que el valor de y0 debe estar dentro del rango de 125 y 23142 para que el código funcione correctamente.
alfa = 0.000082
beta = 24487
gama = 0.1
dias = 90

# Se utiliza un ciclo while para buscar la población mínima viable
while True: 
    for i in range(dias+1): 
        # Se calcula la población del día siguiente utilizando la ecuación dada
        y_day2 = int(alfa * y0* (beta-y0) - gama *y0 - x0) 
        # Si la población del día siguiente no es 0 o negativa, se reduce la población inicial en 1 y se calcula de nuevo
        if y_day2:
            y0-=1 
        else:
            break # Si la población calculada para el día siguiente es igual o menor a cero, el ciclo for actual terminará su ejecución y se detendrá el programa ya que no tiene sentido seguir evaluando una población que ya no es viable. Es decir, se ahorra 'tiempo'.
        
    if not y_day2:
        break # Si se alcanza la población mínima viable, se rompe el ciclo while
    
# Se imprime el resultado
print(f"La poblacion minima viable es: {y0}")