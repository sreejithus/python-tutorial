

s='python coding is easy and fun'

new={i for i in s if i!=' '}
print(new)

#create an new set with onbly vowels 

new={i for i in s if i in 'aeiouAEIOU'}

print(new)


new=[len(i) for i in s.split()]

print(new)


