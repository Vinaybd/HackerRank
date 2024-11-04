# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    records = []
    s= set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        s.add(score)
        
    sec_low_score = sorted(s)[1]
    
    sec_low_names = []
    
    for name,score in records:
        if score == sec_low_score:
            sec_low_names.append(name)
            
    for name in sorted(sec_low_names):
        print(name)
            
   