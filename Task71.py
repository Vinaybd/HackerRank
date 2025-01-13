import re
    
def fun(s):
        # return True if s is a valid email, else return False
    pattern = r"^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    if re.match(pattern, s) is None:
        return False
    else:
        return True
    
def filter_mail(emails):
        return list(filter(fun, emails))
        

if __name__ == '__main__':
    n = int(input("Enter the number of email:"))
    emails = []
    for _ in range(n):
        emails.append(input("Enter your email address:"))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)