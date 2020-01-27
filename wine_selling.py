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


def find_max_price_memo_init(prices):
    memo = [[None] * len(prices) for i in range(len(prices))]
    return find_max_price_memo(prices, 0, len(prices) - 1, memo)


# Find maximum price use memoization
# start -- start in prices array inclusive
# end -- end in prices array inclusive
# memo -- memoization array
def find_max_price_memo(prices, start, end, memo):
    if memo[start][end] is not None:
        return memo[start][end]

    if start == end:
        memo[start][end] = prices[start]
        return prices[start]

    # left
    rest = prices[start+1:end+1]
    price_left = prices[start] + find_max_price_memo(prices, start + 1, end, memo) + sum(rest)

    # right
    rest = prices[start:end]
    price_right = prices[end] + find_max_price_memo(prices, start, end - 1, memo) + sum(rest)

    result = max(price_left, price_right)
    memo[start][end] = result
    return result


# Find maximum price using dynamic programming
# This one was created by modyfing find_max_price_rec to
# use memoization in 2D array.
def find_max_price_dp(price_list):
    prices = [[0] * len(price_list) for i in range(len(price_list))]
    # implement me


def assert_price(f, prices, expected):
    max_price = f(prices)
    msg = "{}: expected {}, {}".format(prices, expected, max_price == expected)
    print(msg)


def cross_validate(f1, f2, prices):
    is_same = (f1(prices) == f2(prices))
    print("{} == {} for {} is {}".format(f1.__name__, f2.__name__, prices, is_same))


def test_suite(f):
    print('testing function: {}'.format(f.__name__))
    for test_case in test_cases:
        assert_price(f, test_case[0], test_case[1])        


def cross_validation_suite(f1, f2):
    for test_case in test_cases:
        cross_validate(f1, f2, test_case[0])
    

test_cases = [([1], 1), ([3], 3), ([1, 2], 5), ([2, 1], 5), ([100, 1], 201), ([1, 2, 3], 14), ([3, 2, 1], 14)]
prices = list(range(1, 10))
expected_price = numpy.dot(prices, prices)
test_cases.append((prices, expected_price))

test_suite(find_max_price_rec)
cross_validation_suite(find_max_price_rec, find_max_price_memo_init)

# it takes 5 seconds on rpi3
#prices = list(range(1, 19))
#expected_price = numpy.dot(prices, prices)
#assert_price(find_max_price_rec, prices, expected_price)

# it takes 18.7  seconds on rpi3
#prices = list(range(1, 21))
#expected_price = numpy.dot(prices, prices)
#assert_price(find_max_price_rec, prices, expected_price)







    
