#!/usr/bin/python3
'''A python script that solves the pascal's triangle problem.
'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing the Pascal’s triangle of n
    '''
    triangle = []
    if n <= 0:
        return triangle
    for row in range(n):
        line = []
        for col in range(i + 1):
            if col == 0 or col == row:
                line.append(1)
            elif row > 0 and col > 0:
                line.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        triangle.append(line)
    return triangle
