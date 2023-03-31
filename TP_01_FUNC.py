# Ejercicio 1 🤪😏😎

# La función chequear() utiliza un ciclo while para pedir al usuario que ingrese un valor, y luego comprueba si es un número real mayor o igual a cero. Si no lo es, el ciclo se repite hasta que se obtenga un valor válido.
def chequear(var):
    """
    La función sirve para chequear los valores que posteriormente se le van a pasar. Si es algo distinto a un número real, se volverá a ejecutar hasta que se obtenga lo que se pide.
    Argumentos:
    - var: Es la variable que se le va a pedir al usuario y que la función va a comprobar si es válida.
    """
    while True:
        try:
            valor = float(input(var))
            if valor >= 0:
                return valor
            else:
                print("Error: no se aceptan números negativos.")
        except:
            print("Error: valor inválido.")

#y0 - Cantidad de peces,
#x0 - Cantidad de pesca diaria.
#alfa - Tasa de reproducción de los peces
#beta - Capacidad del lago (para contener a la población de peces)
#gama - Proporción de peces que son comidos por otros depredadores en el lago
#dias- #Cantidad de días


print(f"Tabla de valores:\n  t_i    |  y_i \n  -------+--------")   # tabla de valores para y0 = 0

def cambio_diario(dias,gama,alfa,beta,y0,x0): 
    """ 
La función cambio_diario calcula el cambio diario de una población de peces a lo largo de varios días, utilizando los valores de y0 (población inicial), alfa, beta, gama, y x0. Devuelve una tabla con los valores de población para cada día.
    
Argumentos:
- dias: un entero que representa el número de días para los que se quiere calcular el cambio diario de la población de peces.
- gama: un número real que representa la tasa de mortalidad de los peces.
- alfa: un número real que representa la tasa de reproducción de los peces.
- beta: un número entero que representa la capacidad máxima de la población de peces.
- y0: un número entero que representa la población inicial de peces.
- x0: un número entero que representa la cantidad de pesca.
    
Devuelve:
- Una lista con la tabla de valores de población para cada día. La lista posteriormente sera "descomprimida" de manera vertical, ya que los valores se almacenan de izquierda a derecha. 
    """
    tabla = []
    for i in range(0,dias+1): 
        y_day2 = alfa * y0 * (beta-y0) - (gama *y0) - x0  # Se calcula el cambio diario de la población de pecesy0>=beta:
        y0 += y_day2 # Se asigna la población nueva al cambio diario de la poblacion        
        if y0 <0: 
            y0 = 0
        elif y0 > beta:
            y0 = beta
                    
        if i == 0:
            tabla.append(f" {i:3d}     | {int(y0-y_day2):5d}")
        else:
            tabla.append(f" {i:3d}     | {int(y0):5d} ")
    return tabla

"""cambio = cambio_diario(dias,gama,alfa,beta,y0,x0)
for c in cambio:
    print(c)"""

def main():
    y0 = chequear("Ingrese y0: ")
    x0 = chequear("Ingrese x: ")
    alfa = chequear("Ingrese alfa: ")
    beta = chequear("Ingrese beta: ")
    while beta > 50000:
        print("El valor de beta no puede ser mayor a 50000.")
        beta = chequear("Ingrese beta: ")
    gama = chequear("Ingrese gama: ")
    dias = int(chequear("Ingrese N: "))

    cambio = cambio_diario(dias,gama,alfa,beta,y0,x0) 
    for c in cambio:
        print(c) #se itera sobre la lista "cambio" e imprime cada elemento en la consola.

if __name__ == "__main__":
    main()
