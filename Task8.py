# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.
#Data types

if __name__ == '__main__':
    n = int(input("Num"))
    l= map(int, input("num").split())
    
    s = set(l)
    l2=list(s)
    
    l2.sort()
    print(l2[-2])


    #another way to solve this
    
    print(sorted(list(set(l)))[-2])