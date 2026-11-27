def occurrences(phrase):
    dico = {}
    for caractère in phrase :
        if caractère in dico :
            dico[caractère] += 1
        else:
            dico[caractère] = 1
    return dico

# Tests
assert occurrences("Bonjour à tous !") == {
    "B": 1, "o": 3, "n": 1, "j": 1, "u": 2,
    "r": 1, " ": 3, "à": 1, "t": 1, "s": 1, "!": 1,
}

assert occurrences("ababbab") == {"a": 3, "b": 4}
