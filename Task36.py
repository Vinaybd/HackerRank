
# You are given two values a and b.
# Perform integer division and print a/b .

for i in range(int(input("Enter the value (3 4):"))):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)