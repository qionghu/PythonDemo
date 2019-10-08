def yearFun(e): 
    return e['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011},
]

print("before sort : ", cars)
cars.sort(key=yearFun)
print("\n cars : ", cars)


def lenFun(e):
    return len(e) 

cars = ["toyota", "bmw", "benz", "linken-do"]
print("\n before sort cars : ", cars)
temp = cars.copy()
temp.sort(key=lenFun)
print("sort default cars : ", temp)
temp_1 = cars.copy()
temp_1.sort(reverse=True, key=lenFun)
print("sort reverse cars : ", temp_1)
