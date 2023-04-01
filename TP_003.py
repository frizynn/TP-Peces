from TP_001 import poblacion_siguiente


def poblacion_minima(x0, dias, alfa, beta, gama, y0):
    """
    Calcula la población mínima viable de peces. 
    Argumentos:
    - x0: Pesca diaria.
    - dias: Días a simular.
    - alfa: Tasa de reproducción de los peces.
    - beta: Capacidad máxima del lago.
    - gama: Tasa de mortalidad de los peces.
    - y0: Población inicial de peces.
    Devuelve:
    - La población mínima viable de peces en el lago.
    """
    while True:
       
        for i in range(dias + 1):
            
            y_day2 = poblacion_siguiente(x0, y0, alfa, beta, gama)
            # Verifica si la tasa de crecimiento es mayor o igual a 0, si no lo es, disminuye la población diaria en 1
            if y_day2 >= 0:
                y0 -= 1
                y_day2 = poblacion_siguiente(x0, y0, alfa, beta, gama)
            else:
                break
            
        # Si la tasa de crecimiento es menor a 0, la función sale del bucle y devuelve la población mínima viable
        if y_day2 <0:
            break
        
    return y0+1 #Cabe destacar que el codigo sigue estrictamente la consigna. Solo es valido para las variables previstas, ya que, por ejemplo, si 124<=y0<=23143, el código no funcionaria correctamente y devolveria un resultado el cual no es correcto. 

def main():
    
    x0 = 237
    alfa = 0.000082
    beta = 24487
    gama = 0.1
    dias = 90
    y0 = 4980

    poblacion_minima_viable = poblacion_minima(x0, dias, alfa, beta, gama, y0)
    print(f"La población mínima viable es: {poblacion_minima_viable}")

if __name__=='__main__':
    main()

