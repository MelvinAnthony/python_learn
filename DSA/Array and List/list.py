import sys

a = []
print(sys.getsizeof(a))  # memory of empty list

a = [1]
print(sys.getsizeof(a))

a = [1, 2]
print(sys.getsizeof(a))
