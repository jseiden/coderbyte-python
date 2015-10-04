def OffLineMinimum(strArr):
    currentNumbers = list()
    result = list()
    for idx,ch in enumerate(strArr):
        if unicode(ch).isnumeric():
            currentNumbers.append(int(ch))
        elif ch == "E":
            currentNumbers = sorted(currentNumbers)
            result.append(currentNumbers[0])
            currentNumbers.pop(0)
            
    return result        
