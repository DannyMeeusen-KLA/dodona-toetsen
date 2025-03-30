def postcode (in_code):

    in_code = int(in_code)
    if (in_code >= 1500 and in_code < 2000) or (in_code >= 3000 and in_code < 3500):
        return "Vlaams-Brabant"
    elif in_code >= 2000 and in_code < 3000:
        return "Antwerpen"
    elif in_code >= 3500 and in_code < 4000:
        return "Limburg"
    elif in_code >= 8000 and in_code < 9000:
        return "West-Vlaanderen"
    elif in_code >= 9000 and in_code < 10000:
        return "Oost-Vlaanderen"
    else:
        return "ongeldig"    