from fractions import Fraction
from functools import reduce
 # complete this line with a reduce statement
def product(fracs):
     
     t=Fraction(reduce(lambda x,y:x*y,fracs))
  
     return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
 

 