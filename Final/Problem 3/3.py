def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    shorter = len(s1) if len(s1) < len(s2) else len(s2)
    result = ""
    for i in range(shorter):
        result += s1[i]
        result += s2[i]
    if len(s1) < len(s2):
        result += s2[shorter:]
    elif len(s1) > len(s2):
        result += s1[shorter:]
    return result
