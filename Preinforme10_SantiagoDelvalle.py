import numpy as np
Presupuesto_Compañia=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])

suma=np.sum(Presupuesto_Compañia)

promedio_0=(Presupuesto_Compañia[0]*100/suma)
promedio_1=(Presupuesto_Compañia[1]*100/suma)
promedio_2=(Presupuesto_Compañia[2]*100/suma)
promedio_3=(Presupuesto_Compañia[3]*100/suma)
promedio_4=(Presupuesto_Compañia[4]*100/suma)
promedio_5=(Presupuesto_Compañia[5]*100/suma)
promedio_6=(Presupuesto_Compañia[6]*100/suma)
promedio_7=(Presupuesto_Compañia[7]*100/suma)
promedio_8=(Presupuesto_Compañia[8]*100/suma)
promedio_9=(Presupuesto_Compañia[9]*100/suma)

Prom_Acumulado=promedio_0 +promedio_1+promedio_2+promedio_3+promedio_4+promedio_5+promedio_6+promedio_7+promedio_8+promedio_9

print ("El promedio del año 2008 con respecto al total fue de",promedio_0)
print ("El promedio del año 2009 con respecto al total fue de",promedio_1)
print ("El promedio del año 2010 con respecto al total fue de",promedio_2)
print ("El promedio del año 2011 con respecto al total fue de",promedio_3)
print ("El promedio del año 2012 con respecto al total fue de",promedio_4)
print ("El promedio del año 2013 con respecto al total fue de",promedio_5)
print ("El promedio del año 2014 con respecto al total fue de",promedio_6)
print ("El promedio del año 2015 con respecto al total fue de",promedio_7)
print ("El promedio del año 2016 con respecto al total fue de",promedio_8)
print ("El promedio del año 2017 con respecto al total fue de",promedio_9)
print ("El promedio acumulado fue de..",Prom_Acumulado)
