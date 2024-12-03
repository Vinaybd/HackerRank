# Enter your code here. Read input from STDIN. Print output to STDOUT


# The first line contains the length of side AB.
# The second line contains the length of side BC .

import math
ab = int(input("Enter the length of AB:"))
bc = int(input("Enter the length of BC:"))
print(round(math.degrees(math.atan(ab / bc))), chr(176), sep="")