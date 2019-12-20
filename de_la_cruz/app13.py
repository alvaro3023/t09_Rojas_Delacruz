import os

DNI=os.sys.argv[1]

if ( len(DNI) == 8 ):
    if ( DNI.isdigit() == True ):
        res = DNI + " es valido"
    else:
        res = DNI + " es invalido (no es un numero)"

else:
    res = DNI + " es invalido (no tiene 8 caracteres)"
#fin_if

print(res)
