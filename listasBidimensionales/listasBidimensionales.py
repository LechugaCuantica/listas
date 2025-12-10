import numpy as np

# Tipos de datos en listas
int = np.array([
    [23, 45, 63],
    [72, 81, 91],
    [56, 64, 37],
    [34, 75, 26]], dtype=int)

float = np.array([
    [4., 5., 6.],
    [7., 8., 9.],
    [10., 11., 12.]
], dtype=float)

complex = np.array([
    [1 + 2j, 3 + 4j, 5 + 6j],
    [7 + 8j, 9 + 10j, 11 + 12j],
    [13 + 14j, 15 + 16j, 17 + 18j]
], dtype=complex)

boolean = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
], dtype=bool)

# Ejemplo de listas bidimensionales en Python
a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])
b = a[0]
print(b)
print(a[0][2])
a[0][1] = 7
print(a)
print(b)
b[2] = 9
print(a[0])
print(b)


# Recorrer una lista bidimensional con bucles for
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()


# Otra forma de recorrer una lista bidimensional con bucles for
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()


# Sumar todos los elementos de una lista bidimensional
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)

# Sumar todos los elementos de una lista bidimensional (otra forma)
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)

# Crear una lista bidimensional con valores iniciales
n = 3
m = 4
a = [[0] * m] * n
a[0][0] = 5
print(a)

# Crear una lista bidimensional correctamente
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m

print(a)


# Leer una lista bidimensional desde la entrada estándar
n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])


# agregar elementos a una lista bidimensional desde la entrada estándar
n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)

    
