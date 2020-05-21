import textdistance

def avg(string1, string2):
    levenshtein = textdistance.levenshtein.normalized_similarity(string1, string2)
    jaccard = textdistance.jaccard(string1, string2)
    cosine = textdistance.cosine(string1, string2)
    return (levenshtein + jaccard + cosine) / 3

def levenshtein(string1, string2):
    levenshtein = textdistance.levenshtein.normalized_similarity(string1, string2)
    return levenshtein

def jaccard(string1, string2):
    jaccard = textdistance.jaccard(string1, string2)
    return jaccard

def cosine(string1, string2):
    cosine = textdistance.cosine(string1, string2)
    return cosine