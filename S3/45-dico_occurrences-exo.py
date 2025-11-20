def occurrences(phrase):
    d = {}
    for lettre in phrase :
        print(lettre)
        if lettre in d :
            d[lettre] = d[lettre]  + 1
        else : 
            d[lettre] = 1
    return d

# Tests
assert occurrences("Bonjour à tous !") == {
    "B": 1, "o": 3, "n": 1, "j": 1, "u": 2,
    "r": 1, " ": 3, "à": 1, "t": 1, "s": 1, "!": 1,
}

assert occurrences("ababbab") == {"a": 3, "b": 4}
