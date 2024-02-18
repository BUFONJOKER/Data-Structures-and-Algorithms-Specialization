def gcd(a,b):
    
    if b == 0:
    
        return a
    
    remainder = a % b
    
    return gcd(b,remainder)

print(gcd(3918848,1653264))