x = -9
y = 8

# without boolean expression
if x < 0:
	if y < 0:
		print('yes')
	else:
		print('no')
else:
	print('no')

# with boolean expression
if x < 0 and y < 0:
	print('yes')
else:
	print('no')


# with ternary-if
print('yes' if x < 0 and y < 0 else 'no')