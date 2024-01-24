# Print the following pattern

# Example pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

def print_number_pattern(rows):
    for pattern in range(1, rows + 1):
        print((str(pattern) + ' ') * pattern)

# Given example:
number_of_rows = 5
print_number_pattern(number_of_rows)