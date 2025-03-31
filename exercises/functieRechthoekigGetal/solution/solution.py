def isRechthoekig(in_getal):

    for factor in range(1, in_getal):
        if factor * (factor+1) == in_getal:
            return True
    return False
    