from random import randint


def ej3a(N):
    totalRolls = []
    for _ in range(N):
        possibleResults = list(range(2, 13))
        numberOfRolls = 0
        while possibleResults != []:
            # D1 + D2
            sumDice = randint(1, 6) + randint(1, 6)
            numberOfRolls += 1
            if sumDice in possibleResults:
                possibleResults.remove(sumDice)
        totalRolls.append(numberOfRolls)
    mean = sum(totalRolls)/N
    stdev = (sum([(x - mean)**2 for x in totalRolls])/(N-1))**0.5
    return (mean, stdev)


iteraciones = [100, 1000, 10000, 100000]
for i in iteraciones:
    print("{} Iteraciones: Media = {}, Desviación estándar = {}".format(
        i, ej3a(i)[0], ej3a(i)[1]))
