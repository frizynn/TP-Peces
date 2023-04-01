from TP_001 import poblacion_siguiente


def calcular_poblacion_minima_viable(x0, dias, alfa, beta, gama, y0):
    
    while True:
       
        for i in range(dias + 1):
            y_day2 = poblacion_siguiente(x0, y0, alfa, beta, gama)
            if y_day2 >= 0:
                y0 -= 1
                y_day2 = poblacion_siguiente(x0, y0, alfa, beta, gama)
            else:
                break
         
        if y_day2 <0:
            break
    return y0+1

def main():
    
    x0 = 237
    alfa = 0.000082
    beta = 24487
    gama = 0.1
    dias = 90
    y0 = 4980

    poblacion_minima_viable = calcular_poblacion_minima_viable(x0, dias, alfa, beta, gama, y0)
    print(f"La población mínima viable es: {poblacion_minima_viable}")

if __name__=='__main__':
    main()