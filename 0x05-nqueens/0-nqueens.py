#!/usr/bin/python3
"""
Module for N Queens.
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    backtrack function to find solution
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[1])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove()


if __name__ == "__main__":
