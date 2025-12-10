# Añadir elementos a una lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insertar un elemento en una posición específica
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Añadir elementos de otra lista
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Añadir elementos de una tupla
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
