#!/usr/bin/python3

# https://www.youtube.com/watch?v=pwpOC1dph6U


# Create all possible ways of selling wines. 
#   0 means sell leftmost wine
#   1 means sell right most wine
def create_all_ways_by_addition(n):    
    if n == 1:
        return ['0']
    
    number_of_ways = 2 ** (n - 1)
    fmt = '{{:0{}b}}0'.format(n - 1)

    return [fmt.format(num) for num in range(number_of_ways)]        
    

create_all_ways = create_all_ways_by_addition
print(create_all_ways(1))
print(create_all_ways(2))
print(create_all_ways(3))

    
