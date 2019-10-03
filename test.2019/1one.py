from math import sqrt

def prime_nembers(n):
	"""
	returns list a of prime numbers up to n
	"""
	a=[]
	for i in range(2, n+1):
	    for j in a:
	        if j > int((sqrt(i)) + 1):
	            a.append(i)
	            break
	        if (i % j == 0):
	            break
	    else:
	        a.append(i)
	return a


print(prime_nembers(1000))
