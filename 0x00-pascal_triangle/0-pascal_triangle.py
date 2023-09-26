#!/usr/bin/python3
'''This module provides a function to generate Pascal's Triangle for a given number of rows'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists: Representing the rows of the Pascal’s triangle
    '''
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists
