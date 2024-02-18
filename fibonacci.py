# Python3 program to calculate
# Fibonacci no. modulo m using
# Pisano Period

# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m 
def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        next_fib_mod_m = (previous + current) % m
        previous = current
        current = next_fib_mod_m
        if previous == 0 and current == 1:
            return i + 1


# Calculate Fn mod m 
def fibonacciModulo(n, m):
	
	# Getting the period
	pisano_period = pisanoPeriod(m)
	
	# Taking mod of N with 
	# period length
	n = n % pisano_period
	
	previous, current = 0, 1
	if n==0:
		return 0
	elif n==1:
		return 1
	for i in range(n-1):
		previous, current = current, previous + current
		
	return (current % m)

# Driver Code

n = 2015
m = 3
# print(fibonacciModulo(n, m))
 
 
 
 
 
def sum_of_square_of_fib(n):
   
    square_z = []
    square_z.append(0)
    square_z.append(1)
    
    z=[]
    z.append(0)
    z.append(1)
    
   

    if n <= 1:
        return n

    else:
        for x in range(2, n + 1):
            result = (z[x - 1]) + (z[x - 2])
            square_result = result**2
            
            z.append(result)
            
            square_z.append(square_result)
            
        
        
        sum = 0
        for i in square_z:
            sum+=i
        
        return sum
    

print(sum_of_square_of_fib(7))
