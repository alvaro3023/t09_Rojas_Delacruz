import Libreria

# Calcular area de la base del cubo
lado1=20
lado2=20
area_base_cubo = Libreria.area_base(lado1,lado2)
print("El area de la base del cubo es:", area_base_cubo)

altura=20

vol_cubo = Libreria.volumen(altura,area_base_cubo)
print("El volumen del cubo es:", vol_cubo)
