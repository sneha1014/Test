def fact(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

num=5
res=fact(num)
print(f"The factorial of {number} is {result}.")
