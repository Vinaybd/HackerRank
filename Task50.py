# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby
if __name__ == "__main__":
    data = input("Enter the input(1222311) :")
    result=[]
    for key, group in groupby(data):
        s=[]
        s.append(len(list(group)))
        s.append(int(key))
        print(tuple(s),end=" ")