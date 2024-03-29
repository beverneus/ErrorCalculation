import math


def nietReproduceerbaar(values: list, latex=False) -> tuple:
    """Takes a list of values, outputs a tuple (average value, absolute error)
    """
    average = sum(values) / len(values)

    n = len(values)
    distancesSquared = [(i - average) ** 2 for i in values]
    significantError = math.sqrt((1 / (n * (n - 1))) * sum(distancesSquared))
    absoluteError = 3 * significantError

    if latex:
        return f"{average} $\pm$ {absoluteError}"
    return average, absoluteError


def LineaireRegressie0(x: list, y: list) -> tuple:
    """Lineaire regressie met fout voor rechte door oorsprong"""
    a = (sum([i * j for i, j in zip(x, y)])) / sum([i**2 for i in x])

    n = len(x)
    standaardAfwijking = math.sqrt(
        (1 / (n - 2)) * sum((j - a * i) ** 2 for i, j in zip(x, y))
    )
    aFout = 3 * standaardAfwijking / math.sqrt(sum([i**2 for i in x]))

    return a, aFout


def LineaireRegressie(x: list, y: list) -> tuple:
    """Lineaire regressie met fout"""
    n = len(x)
    delta = n * sum([i**2 for i in x]) - sum(x) ** 2
    a0 = (
        sum([i**2 for i in x]) * sum(y) - sum(x) * sum([i * j for i, j in zip(x, y)])
    ) / delta

    a1 = (n * sum([i * j for i, j in zip(x, y)]) - sum(x) * sum(y)) / delta

    kwadAfw = math.sqrt(
        (1 / (n - 2)) * sum([(j - a0 - (a1 * i)) ** 2 for i, j in zip(x, y)])
    )
    a0Fout = 3 * kwadAfw * math.sqrt(sum([i**2 for i in x]) / delta)
    a1Fout = 3 * kwadAfw * math.sqrt(n / delta)
    return a0, a1, a0Fout, a1Fout
