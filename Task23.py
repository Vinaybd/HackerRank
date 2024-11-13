# You are given an integer N. Your task is to print an alphabet rangoli of size .
# (Rangoli is a form of Indian folk art based on creation of patterns.)

def print_rangoli(size):
    # your code goes here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    my_list = []
    
    for i in range(size):
        s = "-".join(alphabet[size - 1 : size - 1 - i : -1] + alphabet[size - i - 1: size])
        my_list.append(s.center(4 * size - 3, "-"))
    
    print("\n".join(my_list + my_list[-2::-1]))
        
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

if __name__ == '__main__':
    n = int(input("Enter an number :"))
    print_rangoli(n)