# You are given a string .
# Your task is to find out if the string  contains:
#  alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.



if __name__ == '__main__':
    s = input("Enter a value:")
    alphanum=False; alpha=False; isdigit=False; lower=False; upper=False
    for char in s:
        if char.isalnum():
            alphanum=True
        if char.isalpha():
            alpha=True
        if char.isdigit():
            isdigit=True
        if char.isupper():
            upper=True
        if char.islower():
            lower=True
    print(alphanum)
    print(alpha)
    print(isdigit)
    print(lower)
    print(upper)   
