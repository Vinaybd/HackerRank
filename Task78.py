import re 
import email.utils as email 

n = int(input())

r = re.compile(r'^[a-z](\w|-|\.)*@[a-z]+\.[a-z]{1,3}$')

for i in range(n):
    name,mail = email.parseaddr(input())
        
    if r.match(mail):
        print(email.formataddr((name,mail)))


# Sample input
# 2  
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>