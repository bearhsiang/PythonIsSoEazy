A = input()
B = input()

while True:

	index = A.find(B)
	
	if index == -1:
		break
	
	A = A[:index] + B.upper() + A[index+len(B):]

print(A)