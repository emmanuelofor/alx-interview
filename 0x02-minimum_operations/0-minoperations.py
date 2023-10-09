#!/usr/bin/python3

"""
Function to determine the minimum number of operations required to achieve 'n' characters.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations needed to produce exactly 'n' H characters in a file.
    
    Args:
        n (int): Target number of characters.
        
    Returns:
        int: Minimum number of operations required.
    """
    
    current = 1
    base = 0
    operations = 0
    while current < n:
        difference = n - current
        if (difference % current == 0):
            base = current
            current += base
            operations += 2
        else:
            current += base
            operations += 1
    return operations
