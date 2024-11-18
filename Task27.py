# def merge_the_tools(string, k):
    # your code goes here
def merge_the_tools(string, k):
    text = ""
    for i in string:
        text += "".join(i)
        if len(text) == k:
            for i in range(len(text)):
                s = "".join(sorted(set(text), key=text.index))
            print(s)
            text = ""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)