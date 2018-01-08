# Compute fibonacci taking help of dict to make the process more efficient


def fib_compute(n, d):
    '''

    :param n: number whose fib needs to be found
    :param d: dictionary storing fib of different n
    :return: the value of fib(n)
    '''
    if n in d:
        return d[n]
    else:
        ans = fib_compute(n-1, d) + fib_compute(n-2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 1}