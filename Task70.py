regex_pattern = r""	# Do not delete 'r'.
regex_pattern = r"[.,]"



import re
print("\n".join(re.split(regex_pattern, input())))

# Sample input
# 100,000,000.000