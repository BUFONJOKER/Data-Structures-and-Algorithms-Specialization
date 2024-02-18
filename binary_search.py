def binary_search(array, low, high, key):
    
    if high<low:
        return "Not found"
    
    mid = low + ((high-low)/2)
    mid = round(mid)-1

    value = array[mid]
    
    if key == value:
        return key
    
    elif  key < value:
        return binary_search(array, low, mid - 1, key)
    
    else:
        return binary_search(array, mid+1, high, key)

def sort_array(array):

    for i in range(0,len(array)):

        for j in range(0,len(array)):

            if array[i]<array[j]:
                array[i],array[j] = array[j],array[i]
                

    return array


array = [10,9,8,7,6,5,4,3,2,1]
low = 0
high = len(array) - 1
key = 1

array = sort_array(array)

print(binary_search(array, low, high, key))