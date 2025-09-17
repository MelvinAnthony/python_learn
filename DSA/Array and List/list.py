# Create
arr = [10, 20, 30, 40]

# Access
print("Index 2:", arr[2])

# Update
arr[1] = 99
print("After update:", arr)

# Append
arr.append(50)
print("After append:", arr)

# Insert at index 1
arr.insert(1, 77)
print("After insert:", arr)

# Delete last
arr.pop()
print("After pop remove last value default:", arr)

## delete second value

arr.pop(3)
print("After pop remove 3 value on list usnig index:", arr)

## search the element

search = 99 in arr
print(f"True or False value present or not: {search}")

# Length
print("Length of arr:", len(arr))

