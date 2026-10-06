#give an list

l=[12,4.5,6.8,30,'arun','hello']


# Print floating point numbers
for i in l:
    if type(i) == float:
        print(i)

# Print string values
for i in l:
    if type(i) == str:
        print(i)

# Print integers
for i in l:
    if type(i) == int:
        print(i)


#given an dictionary

d={
     'a':23,'b':25,'c':28,'d':30,'e':22
}

d = {'a': 23, 'b': 25, 'c': 28, 'd': 30, 'e': 22}

for value in d.values():
    if value % 2 == 0:
        print(value)


colors = ['red', 'green', 'blue', 'orange', 'black']

# Print starting letter of each color

for color in colors:
    print(color[0])

# Print last letter of each color

for color in colors:
    print(color[-1])

# Print reverse of each color

for color in colors:
    print(color[::-1])

# Print all colors containing letter 'b'

for color in colors:
    if 'b' in color:
        print(color)
