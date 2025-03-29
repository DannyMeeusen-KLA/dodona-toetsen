def extractPos2 (in_worp):
    return in_worp[1:]

def dartsWorp (in_worp):

    if in_worp == "BULL":
        return 50
    elif in_worp == "SBULL":
        return 25
    elif in_worp[0] == "D":
        return int(extractPos2(in_worp)) * 2
    elif in_worp[0] == "T":
        return int(extractPos2(in_worp)) * 3
    else:
        return int(in_worp)
