import numpy as np
a = np.array([[1,2], [5,6], [8,9]])
# b = np.array([[3,2,1], [7,6,5]])
# c = np.sum(a,b, axis =None)
print("-----------")
print(a)
# print("-----------")
# print(np.linalg.inv(a))
# print("-----------")
# print(np.diag(a))
print("-----------")
boolind = a >2
print(boolind)
print("-----------")
print(np.where(a > 3, a , 'salom'))
print("-----------")


print("-----------")