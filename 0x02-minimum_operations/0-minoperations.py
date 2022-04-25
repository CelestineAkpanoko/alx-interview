#!/usr/bin/python3
'''A Python script that contains a function solves minimum operations task.
'''


def minOperations(n):
    '''Calculates the fewest number of operations 
    needed to result in exactly n H characters in the file.
    '''
    if not isinstance(n, int):
        return 0
    ops_cnt = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_cnt += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_cnt += 2
        elif clipboard > 0:
            done += clipboard
            ops_cnt += 1
    return ops_cnt
