import os
import libreria
densidad= int(os.sys.argv[1])
volumen_del_liquido_desplazado= int(os.sys.argv[2])
aceleracion_por_la_gravedad= int(os.sys.argv[3])
x= libreria.empuje(densidad,volumen_del_liquido_desplazado,aceleracion_por_la_gravedad)
print(x)
