
# Ejercicio 2


x0 = 100

alfa = 0.000082

beta = 24487

gama = 0.1

dias = 90


while True:
    y0 = beta * 0.9 
    x0+=1

    for i in range(1,dias+1):   
        y_day2 = int(alfa * y0* (beta-y0) - gama *y0 - x0)
        y0 += y_day2
        if y0 <= 0:
            x0-=1 #Se hace esta cuenta ya que el anterior x0 es el ultimo en el que el codigo da 0 en el dia 90
            break 
    if y0 <= 0:
        break

print(f"La cantidad máxima de pesca diaria es: {x0}" ) 
   


