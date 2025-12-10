
# Acceder a un elemento de una lista
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Singifica empezar desde el final
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Imprimir un rango de elementos
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# al omitir el primer valor empieza desde el indice 0 y omite el último
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# al omitir el ultimo valor imprime desde el indice marcado hasta el final
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# imprime desde orange hasta melon, no incluye mango
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Comprobar si un valor está en la lista
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
