from fractions import Fraction
from functools import reduce




def product(fracs):
        
    if len(fracs) == 1:
        return fracs[0].numerator, fracs[0].denominator
    else:
        t = reduce( lambda x, y : x * y, fracs )
        return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

# Sample input
# 3
# 1 2
# 3 4
# 10 6