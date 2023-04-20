#!/usr/bin/python3
"""Module for working on creating Pascal's Triangle"""

def pascal_triangle(n):
    """Creates a list of lists of integers representingthe Pascal's triangle of a given integer."""
    list1 = []
    if type(n) is not int or n < 0:
        return list1
    for i in range (n):
        inner_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                inner_list.append(1)
            else:
                inner_list.append((list1[i-1][j-1])+ (list1[i-1][j]))
        list1.append(inner_list)
    return list1
