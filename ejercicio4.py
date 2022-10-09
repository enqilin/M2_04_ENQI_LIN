n1=float(input("Introduce un número real: "))
n2=float(input("Introduce otro número real: "))
n3=float(input("introduce otro número real: "))
listas=[]
listas.extend(n1)
listas.append(n2)
listas.append(n3)
media=sum(listas)/len(listas)
print(media)