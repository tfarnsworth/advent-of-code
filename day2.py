def countCharacters(chars):
    result = {}
    for char in chars:
        if char in result:
            num = result[char]
            num = num + 1
            result[char] = num
        else:
            result[char] = 1
    return result
    
file = open("day-2-input.txt", "r")
twos = 0
threes = 0
for line in file:
    chars = list(line)
    characterCounts = countCharacters(chars)
    for k, v in characterCounts.items():
        if (v == 2):
            twos = twos + 1
            break
    
    for a, b in characterCounts.items():
        if (b == 3):
            threes = threes + 1
            break
total = twos * threes
print total
        

    