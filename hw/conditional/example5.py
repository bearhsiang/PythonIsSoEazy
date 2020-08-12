sentence = input()

if len(sentence) > 20:
	print('lt\'s too long')
elif len(sentence) < 5:
	print('it\'s too short')
else:
	print('wonderful')