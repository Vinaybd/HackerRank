from collections import Counter

if __name__ == '__main__':
    s = input("Enter input(aabbbccc) :")
    d = (sorted(Counter(s).items(), key=lambda item: (-item[1], item[0]))[:3])
    
    for item in d:    
        print(item[0], item[1])