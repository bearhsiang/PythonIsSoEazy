s = input()
s = s.split()
acronym = ''
for word in s:
    acronym += word.upper()[0]
print(acronym)