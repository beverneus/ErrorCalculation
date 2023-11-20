import math

def nietReproduceerbaar(values: list, latex=False) -> tuple:
    '''Takes a list of values, outputs a tuple (average value, absolute error)'''
    
    average = sum(values)/len(values)
    
    n = len(values)
    distancesSquared = [(i - average)**2 for i in values]
    significantError = math.sqrt((1/(n*(n-1))) * sum(distancesSquared))
    absoluteError = 3*significantError
    
    if latex:
        return f'{average} $\pm$ {absoluteError}'
    return average, absoluteError
