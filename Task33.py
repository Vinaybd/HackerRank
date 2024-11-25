
# Now, let's use our knowledge of sets and help Mickey.

# Ms. Gabriel Williams is a botany professor at District College. 
# One day, she asked her student Mickey to compute the average of all the plants with distinct
#  heights in her greenhouse.

def average(array):
    # your code goes here
    distinct_h = set(array)
    avg = round(sum(distinct_h) / len(distinct_h), 3)
    return avg

if __name__ == '__main__':
    n = int(input("Enter the value:"))
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)