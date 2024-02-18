import random

def sort_a_b(a,b):
    
    for i in range(0,len(a)):
        for j in range (0, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
            
            if b[i] > b[j]:
                b[i], b[j] = b[j], b[i]
                
    return a, b

def max_product_pairs_sum(a,b):
    
    if len(a) == 1:
        return a[i] * b[i]
    
    sum = 0
    products = []
    
    a, b = sort_a_b(a,b)
        
    for i in range(0, len(a)):
        
        product = a[i] * b[i]
        sum += product
        products.append(product)
    
    print("a = ",a)
    print("b = ",b)
    print("products = ",products)
    return sum


# a = random.sample(range(-100000,100000),1000)
# b = random.sample(range(100001),1000)
a = [1, 3, -5]
b = [-2, 4, 1]

print(max_product_pairs_sum(a,b))