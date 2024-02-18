def max_num_prizes(n):
    
    sum = 0
    sum_list = []

    if n>2:
        sum = 1
        sum_list.append(1)

    i = 1
    while sum<=n:
        diff = n-sum
        next_i = i+1
        
        if diff >= next_i:
            sum+=next_i
            diff = n-sum
        
            if diff == 0:
                sum_list.append(next_i)
                break
        
            elif diff <= next_i:
                i+=1
                sum-=next_i
        
            else:
                sum_list.append(next_i)        
                i+=1
        
        else:
            i+=1
            
    return sum_list
    
        
    
    
    
n = 125431
result = max_num_prizes(n)
print(len(result))
for i in result:
    print(i, end=" ")

