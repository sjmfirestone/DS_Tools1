def nth_power(n,power):
    '''
    calculates POWAH
    for number up to n (not including n)
    '''
    return [i**power for i in range(n)]

print(nth_power(10,4))
