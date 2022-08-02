import numpy as np

lst = [2,4,6,8,13,2020]
numpy_arr = np.array(lst)
# print(numpy_arr)

lst_2d = [[3, 5, 7, -4, 1], [0, 5, 33, -750, 2]]
numpy_arr_2d = np.array(lst_2d)
# print(numpy_arr_2d)

# print(numpy_arr.shape)
# print(numpy_arr_2d.shape)

# print(numpy_arr.reshape((3,2)))
# print(numpy_arr_2d.reshape((-1, 2)))


# print(numpy_arr[-1:])
# print(numpy_arr_2d[:, 2])

print(np.mean(numpy_arr))
print(np.median(numpy_arr))
print(numpy_arr.min())

print(numpy_arr.max())
