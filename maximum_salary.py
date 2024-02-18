import random
def max_salary(my_list):
    
    new_list = []
    
    for i in range(0,len(my_list)):
        
        max_num = my_list[0]
        
        for j in range (1, len(my_list)):
            
            if my_list[j] > max_num:
                
                max_num = my_list[j]
                
        new_list.append(max_num)
        my_list.remove(max_num)        
                
           
    maximum_salary = ""
    
    for i in new_list:
        maximum_salary+=str(i)
    
    return int(maximum_salary)

my_list = random.sample(range(1,1000), 500)

result = max_salary(my_list)

print(result)