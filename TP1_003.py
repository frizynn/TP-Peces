# Ejercicio 3 - 

x0 = 237

y0 = 4980 # Codigo hecho en base a las constantes provistas. Si y0 fuese menor a 125, el codigo no funcionaria como deberia. Lo hace unicamente con 125<=y0<=23142

alfa = 0.000082

beta = 24487

gama = 0.1

dias = 90

while True: 
    for i in range(1,dias+1): 
        y_day2 = int(alfa * y0* (beta-y0) - gama *y0 - x0) # Cuando el for termina e y0 no es 0, se vuelve a ejecutar. Si es 0, el ciclo while hace el break. Se hace dicha cuenta ya que se va a hacer un ciclo por cada y0.
       
        if y_day2:
            y0-=1       
    if y_day2 <= 0:
        break
    
print(f"La poblacion minima viable es: {y0}") 

