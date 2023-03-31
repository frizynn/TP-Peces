
# Ejercicio 1 🤪😏😎

# Los bucles while a continuacion sirven para tomar valores unicamente validos (es decir, los que corresponden con el calculo). Si se ingresa un valor no valido (por ejemplo, la letra e) va a volver a pedir un valor.

# Los bucles while a continuacion sirven para tomar valores unicamente validos (es decir, los que corresponden con el calculo). Si se ingresa un valor no valido (por ejemplo, la letra e) va a volver a pedir un valor.

#------------------------------- Cantidad de Peces Inicial ---------------------------------

y0 = input("Ingrese y0: ")
#------------------------------ Pesca Díaria ----------------------------------

x0 = input("Ingrese x: ")
    

#------------------------ Tasa de Reproducción ----------------------------------------


alfa = input("Ingrese alfa:")
   

# -------------------------------- Capacidad --------------------------------


beta = input("Ingrese beta: ")
   

#---------------------- Proporcion de peces que son comidos -----------------------------------
gama = input("Ingrese gama: ")

#-------------------------Cantidad de Días 🧟---------------------------------------

dias = input("Ingrese N: ")

#----------------------------------------------------------------

def chequear_int(var):
    while True:
        try:
            var = float(var)
            if var>=0:
                return var
            else:
                var = input('Error, no se aceptan números negativos. Intente de nuevo: ')
                
        except:
            var = input('Error, intente de nuevo')
            continue

                

dias = int(chequear_int(dias))


"""
def check_validez(*funciones):
    if funciones < 0:
        return('Valor invalido. ')
        
print(check_validez(dia()))"""


   # tabla de valores para y0 = 0


for i in range(1,dias+1):    
    y_day2 = alfa * y0 * (beta-y0) - (gama *y0) - x0  # Se calcula el cambio diario de la población de pecesy0>=beta:
    y0 += y_day2 # Se asigna la población nueva al cambio diario de la poblacion        
    if y0 <0: 
        y0 = 0
    elif y0 > beta:
        y0 = beta
                    
    print("  " + str(i) + " "* (6 - len(str(i)))  + "|"  + "  "+ str(int(y0))  ) # tabla de valores para el cambio diario de la poblacion de peces.
     
