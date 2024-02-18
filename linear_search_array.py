def linear_search(array, low, high, key):
    if high<low:
        return "not found"
    
    if array[low] == key:
        return low
    
    return linear_search(array, low + 1, high, key)

array = [1, 2, 9, 90, 12, 35, 55]
low = 0
high = len(array) - 1
key = 90

print(linear_search(array, low, high, key))