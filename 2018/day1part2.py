total = 0
compareTotals = []

def totalInPrevious():
    global total
    global compareTotals
    for freq in compareTotals:
        if (freq == total):
            print "MATCH FOUND"
            print total
            return True
    return False

def mainLoop():
    global total
    global compareTotals
    filename = "day-1-input.txt"
    file = open(filename, "r")
    for line in file:
        num = int(line)
        total += num
        print total
        if (totalInPrevious() == True):
            return True
            break
        else:
            compareTotals.append(total)
    file.close()
    return False

matchingTotal = False
while (matchingTotal == False):
    matchingTotal = mainLoop()

