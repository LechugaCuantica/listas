array = [
    [3, 4, 9, 9, 5],
    [6, 5, 6, 7, 7],
    [6, 1, 4, 7, 4],
    [7, 5, 9, 7, 3],
    [5, 1, 4, 8, 0]
]

# print(array[0][0])
# print(array[1][1])
# print(array[2][2])
# print(array[3][3])
# print(array[4][4])

# for row in range(len(array)):
#     for elem in range(len(array[row])):
#         if row == 0 and elem == 4:
#             print(array[row][elem])
#         elif row == 2 and elem == 2:
#             print(array[row][elem])
for num in range(len(array)):
    elem = num - num - num
    print(array[num][elem])


# for num in array:
#     print(num)
# print(list(enumerate(array)))

# for idx, row in enumerate(array):
#     for idx2, elem in enumerate(row):
#         if idx == idx2:
#             print(' ' * idx2, elem)
#             break
