# First NumPy notebook

import numpy as np

# Array example
a = np.array([1, 2, 3])
print(a)

# Referencing elements
print("Referencing Elements:")
print('a    == {}'.format(a))
print('a[0] == {}'.format(a[0]))
print('a[1] == {}'.format(a[1]))
print('a[2] == {}'.format(a[2]))

# Matrix example
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matrix)
print("matrix[1, 1] =", matrix[1, 1])

# Another example:
my_array = np.array([-3, 0, 3, 16])

print('my_array      == {}'.format(my_array))
print('my_array - 5  == {}'.format(my_array - 5))
print('my_array * 4  == {}'.format(my_array * 4))
print('my_array / 2  == {}'.format(my_array / 2))
print('my_array ** 2 == {}'.format(my_array ** 2))
print('my_array % 2  == {}'.format(my_array % 2))