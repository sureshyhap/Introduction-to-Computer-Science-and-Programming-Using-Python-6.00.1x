def isIn(char, aStr):
    """Checks whether char is in sorted aStr."""
    length = len(aStr)
    mid = length // 2
    if length == 0:
        return False
    elif char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    elif char > aStr[mid]:
        return isIn(char, aStr[mid + 1:])
    
