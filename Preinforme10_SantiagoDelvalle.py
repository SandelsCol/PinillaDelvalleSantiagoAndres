import numpy as np
Presupuesto_Compañia=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])

suma=np.sum(Presupuesto_Compañia)

Año2008=11.984551063729015
Año2009=10.242885868184578
Año2010=12.998548971147347
Año2011=13.333534267101257
Año2012=13.994032267092646
Año2013=14.080146739060233
Año2014=13.634073774268135
Año2015=7.386468833019733
Año2016=1.9866608682922209
Año2017=0.35909734810483573

Deficit_1= Año2009 - Año2008
Deficit_2= Año2010 - Año2009
Deficit_3= Año2011 - Año2010
Deficit_4= Año2012 - Año2011
Deficit_5= Año2013 - Año2012
Deficit_6= Año2014 - Año2013
Deficit_7= Año2015 - Año2014
Deficit_8= Año2016 - Año2015
deficit_9= Año2017 - Año2016

if Deficit_1 > 0:
    print("La compañia aumento sus ganancias en el año 2009 un",Deficit_1,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2009 un",Deficit_1,"%, con respecto al año anterior")


if Deficit_2 > 0:
    print("La compañia aumento sus ganancias en el año 2010 un",Deficit_2,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2010 un",Deficit_2,"%, con respecto al año anterior")


if Deficit_3 > 0:
    print("La compañia aumento sus ganancias en el año 2011 un",Deficit_3,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2011 un",Deficit_3,"%, con respecto al año anterior")


if Deficit_4 > 0:
    print("La compañia aumento sus ganancias en el año 2012 un",Deficit_4,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2012 un",Deficit_4,"%, con respecto al año anterior")


if Deficit_5 > 0:
    print("La compañia aumento sus ganancias en el año 2013 un",Deficit_5,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2013 un",Deficit_5,"%, con respecto al año anterior")


if Deficit_6 > 0:
    print("La compañia aumento sus ganancias en el año 2014 un",Deficit_6,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2014 un",Deficit_6,"%, con respecto al año anterior")


if Deficit_7 > 0:
    print("La compañia aumento sus ganancias en el año 2015 un",Deficit_7,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2015 un",Deficit_7,"%, con respecto al año anterior")


if Deficit_8 > 0:
    print("La compañia aumento sus ganancias en el año 2016 un",Deficit_8,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2016 un",Deficit_8,"%, con respecto al año anterior")


if deficit_9 > 0:
    print("La compañia aumento sus ganancias en el año 2017 un",deficit_9,"%, con respecto al año anterior")
else:
    print("La compañia disminuyo sus ganancias en el año 2017 un",deficit_9,"%, con respecto al año anterior")


