file = open("day-2-input.txt", "r")
lines = file.readlines()
print("length of lines is {0}").format(len(lines))
for i in range(len(lines) - 1):
    currentLine = list(lines[i])
    for j in range(i, len(lines) - 1):
        comparisonLine = list(lines[j])
        diffCount = 0
        commonLetters = ""
        for k in range(len(currentLine)):
            if (currentLine[k] != comparisonLine[k]):
                diffCount = diffCount + 1
            else:
                commonLetters = commonLetters + currentLine[k]
            if (diffCount > 1):
                break
        if (diffCount == 1):
            print("Success! Common letters are {0}").format(commonLetters)
            break


        

    