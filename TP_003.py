
# Ejercicio 2 - Máximo rendimiento posible
x0 = 100
alfa = 0.000082
beta = 24487
gama = 0.1
dias = 90

while True:
    y0 = beta * 0.9 
    x0+=1

    for i in range(1,dias+1):   #
        y_day2 = int(alfa * y0* (beta-y0) - gama *y0 - x0)
        y0 += y_day2
        if y0 <= 0:
            x0-=1 #Se hace esta cuenta ya que el anterior x0 es el ultimo en el que el codigo da 0 en el dia 90
            break 
    if y0 <= 0:
        break
#El código utiliza un bucle while que se ejecuta hasta que la población de peces llega a ser igual o menor a cero, lo que indicaría la extinción de la población. Dentro del bucle, se utiliza un bucle for para simular la población durante los 90 días. En cada día, se calcula la cantidad de peces que mueren debido a la pesca ilegal, representada por la variable x0, y la variación de la población de peces, representada por la variable y_day2. Cuando el bucle for termina y la poblacion no se extinguió para el dia 90, se seuma 1 a la cantiad de pesca, pero con la misma población inical. La cantidad de peces del día actual se actualiza sumando y_day2 a la cantidad de peces del día anterior.

print(f"La cantidad máxima de pesca diaria es: {x0}" ) 
   


