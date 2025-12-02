# Eliminar elementos de una lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Eliminar un elemento en una posición específica
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Eliminar el último elemento de la lista
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Eliminar el último elemento sin especificar el índice
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Eliminar un elemento usando del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Eliminar toda la lista
thislist = ["apple", "banana", "cherry"]
del thislist
