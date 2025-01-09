x, k = map(int, input().split()) 
expression = input() 
print(eval(expression) == k)


# Sample input
# 1 4
# x**3 + x**2 + x + 1