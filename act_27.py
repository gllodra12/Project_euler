import numpy as np
import datetime

def solve_2eq(a,b,c):
    return (-b+np.sqrt(b**2 - 4*a*c))/(2*a)

#print (solve_2eq(1, 1, 41))
    
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime_list=[]
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
             prime_list.append(p)
    return prime_list

b = SieveOfEratosthenes(1000)

def eq(n,a,b):
    return n**2+a*n+b

#print (eq(1,-79, 1601))

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True
a = np.arange(-10**3, 10**3).reshape(-1,1)

num = eq(1, a, b)
valid_nums = list(filter(is_prime_number, np.ravel(num)))
ix = np.isin(num, valid_nums)
mat_bool =ix

n = 2
while np.sum(mat_bool) != 1:
    num = eq(n, a, b)
    valid_nums = list(filter(is_prime_number, np.ravel(num[ix])))
#    print (valid_nums)
    new_ix = np.isin(num, valid_nums)
    ix = new_ix*ix
    mat_bool = ix
    n += 1
#    print (n)
#print ("final")
print (mat_bool)
index_a, index_b = np.where(mat_bool)
print (index_a, index_b)
print (b)
print (b[163])





  



