def extrêmes(valeurs):
    if valeurs == []:
        mini, maxi =None, None
    else:
        mini = valeurs[0]
        maxi = mini
        for x in valeurs:
            if x < mini :
                mini = x
            if maxi < x:
                maxi = x

    return {"min": mini , "max": maxi }

# Tests
assert extrêmes([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {"min": -2, "max": 9}
assert extrêmes([37, 37]) == {"min": 37, "max": 37}
assert extrêmes([]) == {"min": None, "max": None}
