def money_change(n):
    
    denominations_10_5_1 = []
    
    m = n
    
    while m>0:
    
        if m>=10:
            m-=10
            denominations_10_5_1.append(10)
            
        elif m<10 and m>=5:
            m-=5
            denominations_10_5_1.append(5)
            
        elif m<5 and m>=1:
            m-=1
            denominations_10_5_1.append(1)
            
    return denominations_10_5_1

n = 2
result = money_change(n)
print(result)
print(len(result))
    
    