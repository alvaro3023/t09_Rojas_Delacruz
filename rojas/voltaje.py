import os
import libreria

intensidad=int(os.sys.argv[1])
resistencia=int(os.sys.argv[2])
x= libreria.voltaje(intensidad,resistencia)
print(x)
