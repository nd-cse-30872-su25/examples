#!/usr/bin/env python3

# Exercise 04-B: Happy Number

import sys

# Naive version

def is_happy(n: int, seen: set[int]) -> bool:
    if n in seen:                   # Base case: cycles
        return False

    if n == 1:                      # Base case: reaches 1
        return True

    seen.add(n)                     # Mark seen

    squares = sum(x * x for x in map(int, str(n)))
    return is_happy(squares, seen)  # Recurse

# Memoized version

IsHappy = {}                        # Memoization cache

def is_happy_cached(n: int, seen: set[int]) -> bool:
    if n in seen:                   # Base case: cycles
        return False

    if n == 1:                      # Base case: reaches 1
        return True
    
    seen.add(n)                     # Mark seen

    if n not in IsHappy:            # Memoize recursive call
        squares    = sum(x * x for x in map(int, str(n)))
        IsHappy[n] = is_happy_cached(squares, seen)

    return IsHappy[n]

# Main execution

def main() -> None:
    for n in map(int, sys.stdin):
        print('Yes' if is_happy_cached(n, set()) else 'No')

if __name__ == '__main__':
    main()
