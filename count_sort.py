import random
def count_sort(arr):
    min = arr[0]
    max = arr[0]
    
    for i in arr:
        if i>max:
            max = i
    count_arr = []
    for j in range(0, max+1):
        count_arr.append(0)

    for k in arr:
        count_arr[k]+=1

    sorted_arr = []
    for l in range(0,len(count_arr)):
        for m in range(0,count_arr[l]):
            sorted_arr.append(l)
            
    return sorted_arr
            
        
    
arr = [5, 8, 1, 2, 6, 3, 9]

# arr = random.sample(range(400,2000), 1000)

print(count_sort(arr))
