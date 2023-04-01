# Ejercicio 1 

#y0 - Cantidad de peces,
#x0 - Cantidad de pesca diaria.
#alfa - Tasa de reproducción de los peces
#beta - Capacidad del lago (para contener a la población de peces)
#gama - Proporción de peces que son comidos por otros depredadores en el lago
#dias- #Cantidad de días
def chequear(var_name, es_entero=True):
    """
    La función sirve para chequear los valores que posteriormente se le van a pasar. Si es algo distinto al tipo de número especificado, se volverá a ejecutar hasta que se obtenga lo que se pide.
    Argumentos:
    - var_name: Es el nombre de la variable que se le va a pedir al usuario y que la función va a comprobar si es válida.
    - es_entero: Indica si se espera un valor entero o no. Por defecto es True.
    """
    while True:
        try:
            if es_entero:
                var = int(input(var_name))
            else:
                var = float(input(var_name))
            
            if var >= 0:
                return var
            else:
                print("Error: no se aceptan números negativos.")
                
        except:
            print("Error: valor inválido.")

def pedir_valores():
    """ 
    La función pedir_valores pide al usuario los valores de x0, y0, alfa, beta, gama y dias, y se asegura que sean válidos.
    
    Devuelve:
    - Una tupla con los valores ingresados, en el siguiente orden: x0, y0, alfa, beta, gama, dias.
    """
    y0 = chequear("Ingrese y0: ",True)
    x0 = chequear("Ingrese x: ",True)
    alfa = chequear("Ingrese alfa: ",False)
    beta = chequear("Ingrese beta: ",True)
    while beta > 50000:
        print("El valor de beta no puede ser mayor a 50000.") #Se hace esto ya que la capacidad máxima del Lago es 50000
        beta = chequear("Ingrese beta: ",True)
    gama = chequear("Ingrese gama: ",False)
    dias = chequear("Ingrese N: ",True)
    
    return x0, y0, alfa, beta, gama, dias

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
- Una lista con la tabla de valores de población para cada día. La lista posteriormente se va a descomprimir de manera vertical, ya que los valores se almacenan de izquierda a derecha. 
    """
    tabla = []
    poblacion_inicial = y0
    tabla.append(f" {0:3d}     | {int(poblacion_inicial):5d} ")
    
    for i in range(1, dias+1): 
        y_day2 = alfa * y0 * (beta-y0) - (gama *y0) - x0  # Se calcula el cambio diario de la población de peces
        y0 += y_day2 # Se asigna la población nueva al cambio diario de la poblacion        
        if y0 <0: 
            y0 = 0
        elif y0 > beta:
            y0 = beta
            
        tabla.append(f" {i:3d}     | {int(y0):5d} ")
    return tabla



def main():
    """Esta función es la principal del codigo y es un "rejunte" de las demás. Le solicita al usuario que ingrese valores para los parámetros y0, x0, alfa, beta, gama y N. Asegura que beta no sea mayor que 50000. Luego llama a la función cambio_diario para calcular los valores de población para cada día y los imprime en la consola en forma de tabla."""
    x0, y0, alfa, beta, gama, dias = pedir_valores()
    print(f"Tabla de valores:\n  t_i    |  y_i \n  -------+--------")   # tabla de valores para y0 = 0
    cambio = cambio_diario(dias,gama,alfa,beta,y0,x0) 
    for c in cambio:
        print(c) # Se itera sobre la lista "cambio" e imprime cada elemento en la consola.

if __name__ == "__main__":
    main()
