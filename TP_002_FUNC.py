
# Ejercicio 2
from TP_01_FUNC import cambio_diario 


x0 = 100

alfa = 0.000082

beta = 24487

gama = 0.1

dias = 90


while True:
    y0 = beta * 0.9 
    x0+=1
    
    cambio_diario(dias,gama,alfa,beta,y0,x0)
          
    if y0 <= 0:
        break

print(f"La cantidad máxima de pesca diaria es: {x0}" ) 
   
# 11111 es el maximo de pesca para que no se extinga la poblacion


