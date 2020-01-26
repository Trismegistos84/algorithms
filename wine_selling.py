#!/usr/bin/python3

# https://www.youtube.com/watch?v=pwpOC1dph6U

# Scheme of selling wine is just some path in binary 
# tree. Tree has height number_of_wines - 1. We choose
# only n - 1 wines because if we have to sell last wine
# we do not really has choice to go left or right.

import numpy


# Create all possible ways of selling wines. 
#   0 means sell leftmost wine
#   1 means sell right most wine
def create_all_ways_by_addition(n):
    if n == 1:
        return ['0']
    
    number_of_ways = 2 ** (n - 1)
    fmt = '{{:0{}b}}0'.format(n - 1)

    return [fmt.format(num) for num in range(number_of_ways)]        


# Find maximum price recursively
def find_max_price_rec(prices):
    if len(prices) == 0:
        return 0

    # left
    rest = prices[1:]
    price_left = prices[0] + find_max_price_rec(rest) + sum(rest)

    # right
    rest = prices[:-1]
    price_right = prices[-1] + find_max_price_rec(rest) + sum(rest)

    return max(price_left, price_right)


def assert_price(f, prices, expected):
    max_price = f(prices)
    msg = "{}: expected {}, {}".format(prices, expected, max_price == expected)
    print(msg)


def test_suite(f):
    print('testing function: {}'.format(f.__name__))
    assert_price(f, [1], 1)
    assert_price(f, [3], 3)
    assert_price(f, [1, 2], 5)
    assert_price(f, [2, 1], 5)
    assert_price(f, [100, 1], 201)

    assert_price(f, [1, 2, 3], 14)
    assert_price(f, [3, 2, 1], 14)

    prices = list(range(1, 10))
    expected_price = numpy.dot(prices, prices)
    assert_price(find_max_price_rec, prices, expected_price)


test_suite(find_max_price_rec)


# it takes 11 seconds
#prices = list(range(1, 25))
#expected_price = numpy.dot(prices, prices)
#assert_price(find_max_price_rec, prices, expected_price)

# it takes 45 seconds
#prices = list(range(1, 27))
#expected_price = numpy.dot(prices, prices)
#assert_price(find_max_price_rec, prices, expected_price)







    
