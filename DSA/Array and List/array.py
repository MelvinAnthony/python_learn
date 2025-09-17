import array

arr_call = array.array
arr = arr_call('i',[1,2,3,4,5])
print(arr)


## Access Element
A_array =arr[2]
print(f"Array Index of 2 was: {arr[2]}")

## Update Element

arr[2] = 1
print(f"Update Element on 2 index: {arr}")

## Insert Element 

arr.insert(2,99)
print(f"Insert Element on 2 index: {arr}")

## Delete Element
arr.remove(5)

print(f"Remove the element vlaues remove the 5 value on my list : {arr}")

## Append Element
arr.append(60)
print(f"apeend the value on last default : {arr}")
