# You are given a string S and width W .
# Your task is to wrap the string into a paragraph of width .


import textwrap

def wrap(string, max_width):
     return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input("Enter an string:"), int(input("Enter a number:"))
    result = wrap(string, max_width)
    print(result)