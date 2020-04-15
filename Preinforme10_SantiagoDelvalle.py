import numpy as np
Presupuesto_Compañia=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])

Deficit= Presupuesto_Compañia[9]-Presupuesto_Compañia[8]
Deficit_2= -(Deficit)

print("""La diferencia de la Utilidad Operacional Anual de Kellog's Colombia 
entre los años 2017 y 2016 fue de""",Deficit,""",Es decir , La compañia perdio ganancias anuales de""",Deficit_2,"""Millones de pesos colombianos""")


