# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
number_list = tuple(map(int, input().split()))
print(all(number>=0 for number in number_list) and any(str(number) == str(number)[::-1] for number in number_list))




# sample input
# 5
# 12 9 61 5 14 