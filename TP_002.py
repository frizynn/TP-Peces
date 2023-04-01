from TP_001 import poblacion_siguiente

def calcular_poblacion_peces(y0, alfa, beta, gama, x0, dias):
    """
    Calcula la población de peces en función de la cantidad de pesca diaria durante un número determinado de días.
    Se verifica si la población de peces es mayor que 0 después de los 90 días de pesca. Si la población es mayor que 0, la función devuelve True y el valor de la población de peces. Si la población es menor o igual a 0, la función devuelve False y la cantidad máxima de pesca diaria que se puede realizar sin llevar a la extinción de los peces.
    Argumentos:
    - y0: Población inicial de peces.
    - alfa: Tasa de reproducción de los peces.
    - beta: Capacidad máxima del lago.
    - gama: Tasa de mortalidad de los peces.
    - x0: Cantidad de pesca diaria.
    - dias: Cantidad de días a simular.
    Devuelve:
    - La población final de peces.
    - Un booleano dependiendo el resultado de la poblacion final.
    """
    for i in range(1, dias + 1):
        # Cálculo de la población de peces al día siguiente, teniendo en cuenta la cantidad de pesca diaria
        y_day2 = poblacion_siguiente(x0, y0, alfa, beta, gama)
        y0 += y_day2

        # Verificación si la población de peces sigue siendo mayor que 0
        if y0 <= 0:
            return False, x0 - 1 # Se hace esta cuenta ya que el anterior x0 es el último en el que el código da 0 en el día 90

    return True, y0


def max_pesca():
    """
    Busca la cantidad máxima de pesca diaria sin que se extingan los peces. Se va a llamar a 'calcular_poblacion_peces()' y se va a hacer el cálculo hasta que de 0. Por cada iteración que no de 0, se suma 1 a la pesca diaria y se vuelve a ejecutar la funcion utilizando ese x0 por 90 dias. Si de vuelta no es 0, se suma 1 a x0 y así sucesivamente. A 'exito' se le asigna un bool y a poblacion_final el resultado de calcular_poblacion_peces(). 

    Devuelve:
    - La cantidad máxima de pesca diaria que se puede realizar sin llevar a la extinción de los peces.
    """
    x0 = 0 
    alfa = 0.000082 
    beta = 24487
    gama = 0.1 
    dias = 90 

    # Ciclo principal para buscar la cantidad máxima de pesca diaria sin extinguir la población.
    while True:
        y0 = beta * 0.9 
        exito, poblacion_final = calcular_poblacion_peces(y0, alfa, beta, gama, x0, dias) 
        if not exito: # exito necesita ser false para que el bucle termine (if not False), ya que en calcular_poblacion_peces se definió que si y0 es 0 el bucle termina y se devuelve false. 
            break
        x0 += 1 
    return poblacion_final


def main():
    max_pesca_diaria = max_pesca()
    print(f"La cantidad máxima de pesca diaria es: {max_pesca_diaria}" )


if __name__ == "__main__":
    main()
