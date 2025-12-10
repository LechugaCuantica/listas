# Comprensión de listas
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Crear una nueva lista con frutas que contienen la letra "a"
newlist = [x for x in fruits if "a" in x]

print(newlist)

# Crear una nueva lista con frutas que no sean "apple"
newlist = [x for x in fruits if x != "apple"]

# Crear una nueva lista con los números al cuadrado
newlist = [x for x in fruits]

# Crear una nueva lista con números del 0 al 9
newlist = [x for x in range(10)]

# Crear una nueva lista con números menores a 5
newlist = [x for x in range(10) if x < 5]

# Crear una nueva lista con las frutas en mayúsculas
newlist = [x.upper() for x in fruits]

# Crear una nueva lista con la longitud de cada fruta
newlist = ['hello' for x in fruits]

# Crear una nueva lista reemplazando "banana" por "orange"
newlist = [x if x != "banana" else "orange" for x in fruits]
