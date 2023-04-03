#!/usr/bin/python3
""" This module is the solution for N-Queen
puzzle
"""


def safety(squ, nqu):
    """ if queens are safe from each other
    Arg:
        squ: 1st parameter arr has qu positions
        nqu: 2nd parameter queen num
    Return:
        True: are safe
        False: are not safe
    """
    for x in range(nqu):
        if squ[x] == squ[nqu]:
            return False
        if abs(squ[x] - squ[nqu]) == abs(x - nqu):
            return False
    return True


def res(squ, nqu):
    """ Prints list with the positions
    Arg:
        squ: arr has qu positions
        nqu: queen num
    Return:
        None
    """
    r = []
    for x in range(nqu):
        r.append([x, squ[x]])

    print(r)


def qu(squ, nqu):
    """ executes the functions
    Arg:
        squ: arr has qu positions
        nqu: queen num
    Return:
        None
    """
    if nqu is len(squ):
        res(squ, nqu)
        return

    squ[nqu] = -1
    while((squ[nqu] < len(squ) - 1)):
        squ[nqu] += 1

        if safety(squ, nqu) is True:
            if nqu is not len(squ):
                qu(squ, nqu + 1)


def solqu(s):
    """ Backtracking algo
    Arg:
        s: size of board
    """
    squ = [-1 for i in range(s)]

    qu(squ, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        s = int(sys.argv[1])
    except Exception as e:
        e = "N must be a number"
        print(e)
        sys.exit(1)

    if s < 4:
        print("N must be at least 4")
        sys.exit(1)

    solqu(s)
