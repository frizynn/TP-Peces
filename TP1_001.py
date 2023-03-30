# Ejercicio 1 🤪😏😎

# Los bucles while a continuacion sirven para tomar valores unicamente validos (es decir, los que corresponden con el calculo). Si se ingresa un valor no valido (por ejemplo, la letra e) va a volver a pedir un valor.
while True:
    beta = input("Ingrese capacidad de lago: ")
    try:
        beta = int(beta)
        if beta>=0 and beta<=50000:
            break
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')
#------------------------------- Cantidad de Peces Inicial ---------------------------------

while True:
    y0 = input("Ingrese cantidad inicial de peces: ")
    try:
        y0 = int(y0)
        if y0>=0 and y0<=beta:
            break
        elif y0 >beta:
            print('La cantidad inicial de peces no puede ser mayor a la capacidad maxima del lago. Intente de nuevo.')
            continue
            
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')


#------------------------------ Pesca Díaria ----------------------------------

while True:
    x0 = input("Ingrese la pesca diaria: ")
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
    alfa = input("Ingrese tasa de reproduccion:")
    try:
        alfa = float(alfa)
        if alfa>=0:
            break
        else:
            print('Valor no válido. Intente de nuevo: ')
            continue
        
    except:
        print('Error, intente de nuevo: ')

#---------------------- Proporcion de peces que son comidos -----------------------------------

while True:
    gama = input("Ingrese proporcion de peces que son comidos: ")
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
    dias = input("Ingrese cantidad de días: ")
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

print(f"Tabla de valores:\n  t_i    |  y_i \n  -------+--------\n {0:2d}      |  {y0:5d}")   # tabla de valores para y0 = 0


for i in range(1,dias+1):    
    y_day2 = alfa * y0 * (beta-y0) - (gama *y0) - x0  # Se calcula el cambio diario de la población de pecesy0>=beta:
    y0 += y_day2 # Se asigna la población nueva al cambio diario de la poblacion        
    if y0 <0: 
        y0 = 0
    elif y0 > beta:
        y0 = beta
                
    
    print(f" {i:2d}      |  {int(y0):5d} ")




"""
    
 $$$$$$\                                     $$\                  $$$$$$\            $$\ $$\ $$\           
$$  __$$\                                    $$ |                $$  __$$\           \__|$$ |$$ |          
$$ /  \__| $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\        $$ /  \__|$$\   $$\ $$\ $$ |$$ | $$$$$$\  
$$ |$$$$\ $$  __$$\ \____$$\ $$  __$$\ $$  __$$ |$$  __$$\       $$ |$$$$\ $$ |  $$ |$$ |$$ |$$ |$$  __$$\ 
$$ |\_$$ |$$ |  \__|$$$$$$$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |      $$ |\_$$ |$$ |  $$ |$$ |$$ |$$ |$$$$$$$$ |
$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |$$   ____|
\$$$$$$  |$$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\       \$$$$$$  |\$$$$$$  |$$ |$$ |$$ |\$$$$$$$\ 
 \______/ \__|      \_______|\__|  \__| \_______| \_______|       \______/  \______/ \__|\__|\__| \_______|
                                                                                                           
                                                                                                           
                                                                                                           """