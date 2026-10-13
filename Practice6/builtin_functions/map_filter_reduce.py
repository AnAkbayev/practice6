from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map(): apply a function to every item
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)

# filter(): keep items that satisfy a condition
evens = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce(): combine items into one result
total = reduce(lambda accumulator, number: accumulator + number, numbers, 0)
product = reduce(lambda accumulator, number: accumulator * number, numbers, 1)
print("Sum with reduce:", total)
print("Product with reduce:", product)
