s = input()

is_palindrome = True
for i in range(len(s)):
	if s[i] != s[-1-i]:
		is_palindrome = False
		break
	
if is_palindrome:
	print('yes')
else:
	print('no')

# method2
if s[::-1] == s:
	print('yes')
else:
	print('no')