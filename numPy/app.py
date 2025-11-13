import numpy as np
print(np.__version__)

zero_arr = np.zeros((2, 3), dtype=bool)
print(zero_arr)

one_arr = np.ones((4, 4), dtype=int)
print(one_arr)

x_arr = np.full((4,2), 5.4, dtype=float)
print(x_arr)

step_arr = np.arange(1, 7, 2)
print(step_arr)

between_arr = np.linspace(0,1, 5, dtype=float)
print(between_arr)

eye_arr =np.eye(3, dtype=int) # bosh dioganal 1 matritsa.
print(eye_arr)

arr = np.array([[1,4,3,5], [4,6,7,3], [1,7,9,8]])
print(arr)
asd = arr.reshape(4,3) # shaklni o'zgartiradi.
print(asd)
t_arr = np.array([[1,2,3,4,5]])
print(t_arr.T)
di_arr = arr.flatten() # birlik shaklga o'tkazadi.
print(di_arr)

A = np.array([[1,2],
              [3,4]])
B = np.array([[6,7],
              [8,9]])

print(np.dot(A,B))
print(np.linalg.inv(A)) # Teskari matritsa.
print(np.linalg.det(B))
print(np.trace(A), np.trace(B))



