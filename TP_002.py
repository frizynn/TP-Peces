# Definición de los valores iniciales
x0 = 100 # Cantidad de pesca diaria inicial
alfa = 0.000082 # Coeficiente alfa para el cálculo de la población de peces
beta = 24487 # Capacidad máxima de la población de peces
gama = 0.1 # Tasa de mortalidad diaria de los peces
dias = 90 # Cantidad de días a simular

# Ciclo principal para buscar la cantidad máxima de pesca diaria sin llevar a la extinción de los peces
while True:
    y0 = beta * 0.9 # Población inicial de peces, en este caso se toma el 90% de la capacidad máxima
    x0 += 1 # Se comienza con una cantidad de pesca diaria mayor que la inicial

    # Ciclo que simula los 90 días de pesca
    for i in range(1, dias + 1):
        # Cálculo de la población de peces al día siguiente, teniendo en cuenta la cantidad de pesca diaria
        y_day2 = int(alfa * y0 * (beta - y0) - gama * y0 - x0)
        y0 += y_day2

        # Verificación si la población de peces sigue siendo mayor que 0
        if y0 <= 0:
            # Si la población de peces se vuelve menor o igual a 0, se interrumpe la simulación y se calcula la cantidad máxima de pesca diaria que se puede realizar sin llevar a la extinción de los peces
            x0 -= 1 # Se hace esta cuenta ya que el anterior x0 es el último en el que el código da 0 en el día 90
            break 

    # Verificación si la población de peces sigue siendo mayor que 0 después de los 90 días de pesca
    if y0 <= 0:
        break

# Impresión del resultado final
print(f"La cantidad máxima de pesca diaria es: {x0}" ) 
