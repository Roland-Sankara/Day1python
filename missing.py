listA = [1,4,7,9,14]


def list_1(t):
    missing = []
    for x in range(t[0],t[-1]):
        if x not in t:
            missing.append(x)
    return missing 


print(list_1(listA))