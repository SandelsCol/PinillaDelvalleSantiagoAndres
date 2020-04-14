import numpy as np
Presupuesto_Compañia=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])

Promedio_1= (Presupuesto_Compañia[0] + Presupuesto_Compañia[1])/2
Promedio_2= (Presupuesto_Compañia[8] + Presupuesto_Compañia[9])/2
Diferencia = (Promedio_1 - Promedio_2)

print ("El promedio entre los años 2008 y 2009 es..",Promedio_1)
print ("El promedio entre los años 2016 y 2017 es..",Promedio_2)
print("La diferencia entre los dos ciclos es de..",Diferencia)



