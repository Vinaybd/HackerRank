# Read a given string, change the character at a given
# index and then print the modified string.




def mutate_string(string, position, character):
    out = string[:position] + character + string[position+1:]
    return out
    

if __name__ == '__main__':
    s = input("Enter a string")
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)