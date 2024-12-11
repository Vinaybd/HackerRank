# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input("Enter the number:")) 
countries=set() 
for i in range(n): 
    name=input("Enter the country names:") 
    countries.add(name) 
print(len(countries))