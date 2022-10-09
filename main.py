set={"coche","autobus","bici","camion"}
vehiculos={"brand":"ford","model": "mostang","year":"1964"}
print(set,vehiculos)

print(vehiculos["brand"][0:5])
vehiculos["brand"]="volvo"
print(set,vehiculos)
print(len(set))
print(len(vehiculos))
print("coche" in set)
print("avion" in set)
print("model" in vehiculos)
print("volvo" in vehiculos)
set.add('tren')
set.update(['metro','barca'])
print(set)
set.remove("bici")
set.discard("camion")
print(set)



n1=float(input("Introduce un número real: "))
n2=float(input("Introduce otro número real: "))
n3=float(input("introduce otro número real: "))
listas=[]
listas.append(n1),(n2),(n3)
listas.append(n2)
listas.append(n3)
print(listas)
sumatorio=sum(listas[-3:])
print(sumatorio)

media=sum(listas)/len(listas)
print(media)

colores=["azul", "amarillo", "rojo", "verde"]
cosas=("casa", "puerta ", "reloj", "mesa", "silla")
print(colores)
print(cosas)
print(colores[1])
print(cosas[3])
colores[2]= "naranja"
print(colores,cosas)
print("verde"in colores)
print("rosa" in colores)
print(2 in cosas)
print('casa' in cosas)
colores.append("violeta")
print(colores)
cosas.append("muebles")#
