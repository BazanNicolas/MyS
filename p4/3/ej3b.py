from random import randint

# estime la probabilidad de que N sea por lo menos 15


def ej3b15(N):
    totalRolls = 0
    for _ in range(N):
        possibleResults = list(range(2, 13))
        numberOfRolls = 0
        while possibleResults != []:
            # D1 + D2
            sumDice = randint(1, 6) + randint(1, 6)
            numberOfRolls += 1
            if sumDice in possibleResults:
                possibleResults.remove(sumDice)
        if numberOfRolls >= 15:
            totalRolls += 1
    return totalRolls/N

# estime la probabilidad de que N sea a lo sumo 9


def ej3b9(N):
    totalRolls = 0
    for _ in range(N):
        possibleResults = list(range(2, 13))
        numberOfRolls = 0
        while possibleResults != []:
            # D1 + D2
            sumDice = randint(1, 6) + randint(1, 6)
            numberOfRolls += 1
            if sumDice in possibleResults:
                possibleResults.remove(sumDice)
        if numberOfRolls <= 9:
            totalRolls += 1
    return totalRolls/N


iteraciones = [100, 1000, 10000, 100000]
for i in iteraciones:
    print("{} Iteraciones: Probabilidad de que N sea por lo menos 15 = {}, Probabilidad de que N sea a lo sumo 9 = {}".format(
        i, ej3b15(i), ej3b9(i)))
