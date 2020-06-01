def is_inverse(word1, word2):
    if len(word1) != len (word2):
        return False
    i = 0
    j = len(word1)-1
    while j >= 0:
        if word1[i].upper() != word2[j].upper():
            return False
        i += 1
        j -= 1
    return True

print(is_inverse("Wow","wow"))
