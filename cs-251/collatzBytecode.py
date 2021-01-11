import dis

def collatz(n):
	while n>1:
		print(n, end=' ')
		if n%2:
			n = 3*n+1 #n is odd
		else:
			n = n//2
	print(1)

dis.dis(collatz)