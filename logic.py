import random

def validate_probabilities(p):
    if len(p) != 6:
        raise Exception("need 6 values")

    for x in p:
        if type(x) != int and type(x) != float:
            raise Exception("not number")
        if x < 0:
            raise Exception("negative not allowed")

    if round(sum(p), 5) != 1.0:
        raise Exception("sum must be 1")

def roll_dice(p, n):
    result = []
    for i in range(n):
        r = random.choices([1,2,3,4,5,6], weights=p)[0]
        result.append(r)
    return result