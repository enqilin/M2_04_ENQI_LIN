colores=["azul", "amarillo", "rojo", "verde"]
cosas=("casa", "puerta ", "reloj", "mesa", "sillla")
print(colores)
print(cosas)
print(colores[1])#mostrar el segundo indice
print(cosas[3])
colores[2]= "naranja"#cambiar el rojo a naranja
print(colores,cosas)
print(len(colores,cosas))
print("verde"in colores)
print("rosa" in colores)
print(2 in cosas)
print('casa' in cosas)
colores.append("violeta")
print(colores)
cosas.append("muebles")#sale error
print(cosas)
colores.pop(1)
print(colores)
cosas.pop(4)#tupla no se puede eliminar elemento
print(cosas)
