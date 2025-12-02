
# Recorrer una lista
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Recorrer una lista usando índices
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Recorrer una lista usando un bucle while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Usar una comprensión de listas para recorrer una lista
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
