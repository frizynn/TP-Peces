# Ejercicio 1 🤪😏😎

# Los bucles while a continuacion sirven para tomar valores unicamente validos (es decir, los que corresponden con el calculo). Si se ingresa un valor no valido (por ejemplo, la letra e) va a volver a pedir un valor.

#------------------------------- Cantidad de Peces Inicial ---------------------------------

while True:
    y0 = input("Ingrese y0: ")
    try:
        y0 = int(y0)
        if y0>=0:
            break
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')
#------------------------------ Pesca Díaria ----------------------------------

while True:
    x0 = input("Ingrese x: ")
    try:
        x0 = int(x0)
        if x0>=0:
            break
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')

#------------------------ Tasa de Reproducción ----------------------------------------

while True:
    alfa = input("Ingrese alfa:")
    try:
        alfa = float(alfa)
        if alfa>=0:
            break
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')

# -------------------------------- Capacidad --------------------------------

while True:
    beta = input("Ingrese beta: ")
    try:
        beta = int(beta)
        if beta>=0 and beta<=50000:
            break
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')

#---------------------- Proporcion de peces que son comidos -----------------------------------

while True:
    gama = input("Ingrese gama: ")
    try:
        gama = float(gama)
        if gama>=0:
            break
        else:
            print('Error, no se aceptan números negativos. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')

#-------------------------Cantidad de Días 🧟---------------------------------------

while True:
    dias = input("Ingrese N: ")
    try:
        dias = int(dias)
        if dias>=0:
            break
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')

#----------------------------------------------------------------

print(f"Tabla de valores:\n  t_i    |  y_i \n  -------+--------")   # tabla de valores para y0 = 0


for i in range(0,dias+1): 
    length = len(str(y0))
    y_day2 = alfa * y0 * (beta-y0) - (gama *y0) - x0  # Se calcula el cambio diario de la población de pecesy0>=beta:
    y0 += y_day2 # Se asigna la población nueva al cambio diario de la poblacion        
    if y0 <0: 
        y0 = 0
    elif y0 > beta:
        y0 = beta
                
    if i == 0:
        print(f" {i:3d}     | {int(y0-y_day2):5d}")
    else:
        print(f" {i:3d}     | {int(y0):5d} ")




"""
Preguntar como poner el blucle en una funcion y que no se ejecute todo lo anterior
    
 $$$$$$\                                     $$\                  $$$$$$\            $$\ $$\ $$\           
$$  __$$\                                    $$ |                $$  __$$\           \__|$$ |$$ |          
$$ /  \__| $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\        $$ /  \__|$$\   $$\ $$\ $$ |$$ | $$$$$$\  
$$ |$$$$\ $$  __$$\ \____$$\ $$  __$$\ $$  __$$ |$$  __$$\       $$ |$$$$\ $$ |  $$ |$$ |$$ |$$ |$$  __$$\ 
$$ |\_$$ |$$ |  \__|$$$$$$$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |      $$ |\_$$ |$$ |  $$ |$$ |$$ |$$ |$$$$$$$$ |
$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |$$   ____|
\$$$$$$  |$$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\       \$$$$$$  |\$$$$$$  |$$ |$$ |$$ |\$$$$$$$\ 
 \______/ \__|      \_______|\__|  \__| \_______| \_______|       \______/  \______/ \__|\__|\__| \_______|
                                                                                                           
                                                                                                           
                                                                                                           """