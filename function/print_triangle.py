def print_tri(N):
	if N == 0:
		return 0
	print('*'*N)
	return N + print_tri(N-1)

num = print_tri(10)
print('using', num, 'of star.')