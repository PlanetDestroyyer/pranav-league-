def fic(n):
	if n == 1 or n == 2:
		return  1
	n_1 = fic(n-1)
	n_2 = fic(n-2)
	outout = n_1+n_2
	return  outout
n = int(input())
for n in n:
	print(fic(n))