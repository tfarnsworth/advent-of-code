filename = "day-1-input.txt"
file = open(filename, "r")
total = 0
for line in file:
    num = int(line)
    total += num
print total
