set={"coche","autobus","bici","camion"}
vehiculos={"brand":"ford","model": "mostang","year":"1964"}
print(set,vehiculos)
print(vehiculos["brand"][0:5])
vehiculos["brand"]="volvo"
print(len(set))
print(len(vehiculos))
print("coche" in set)
print("avion" in set)
print("model" in vehiculos)
print("volvo" in vehiculos)
set.add('tren')
set.update(['metro','barca'])
print(set,vehiculos)
set.remove("bici")
set.dicard("camion")
print(set)