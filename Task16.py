# string split and join 

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    print(line)
    # write your code here

if __name__ == '__main__':
    line = input("Enter your text :")
    result = split_and_join(line)
    # print(line)
    # print(result)