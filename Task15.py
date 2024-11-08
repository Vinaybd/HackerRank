# You are given a string and your task is to swap cases.
#  In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input("Enter a string :")
    result = swap_case(s)
    print(result)


#ANOTHER METHOD OR APPROCH

def swap_case(s):
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s)