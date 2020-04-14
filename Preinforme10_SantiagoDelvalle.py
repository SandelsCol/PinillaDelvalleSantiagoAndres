import numpy as np
Presupuesto_Compañia=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])

media= np.mean(Presupuesto_Compañia)
mediana= np.median(Presupuesto_Compañia)
diferencia = media - mediana

print ("La media es de",media)
print ("La mediana es de",mediana)
print ("La diferencia entre la media y la mediana es de",diferencia)