numbers = [1, 8, 3, 12, 6]

def find_max(numbers):
    max = 0
    for c in (numbers):
        if c > max: max = c
    return max

print (find_max(numbers))

help(enumerate)