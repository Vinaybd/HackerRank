# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input()
vowels = "aeiouAEIOU"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

pattern = r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])'

matches = re.findall(pattern, s)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)


# Sample input
# rabcdeefgyYhFjkIoomnpOeorteeeeet