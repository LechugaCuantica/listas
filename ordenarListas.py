# Ordena alfabeticamente la lista
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Ordena la lista de números de menor a mayor
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Ordena la lista descendentemente
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Ordena la lista de números de mayor a menor
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Ordena la lista según la función personalizada
# ordena los números a lo más cercanos a 50


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Ordena la lista sin importar mayúsculas o minúsculas
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Invierte el orden de la lista
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
