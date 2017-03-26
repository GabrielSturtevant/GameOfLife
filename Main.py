#!/usr/bin/python

import Board
import os
import time
import sys
from Loader import glider_gun


def check(a, b):
    if len(a) == len(b):
        for f in range(len(a)):
            if a[f] != b[f]:
                return False
    else:
        return False
    return True


dimension = 15
if len(sys.argv) > 1:
    dimension = int(sys.argv[1])

foo = Board.Board(dimension)
# for key, cell in foo.board.iteritems():
#     cell.state = False
# for i in range(len(glider_gun)):
#     for j in range(len(glider_gun[i])):
#         key = str(i)+','+str(j)
#         foo.board[key].state = glider_gun[i][j] == 1

first = []
second = []
turns = 0
firstup = True
while True:
    turns += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    foo.print_printable()
    if turns == 1:
        first = foo.printable[:]
        foo.print_board()
    if turns == 2:
        second = first[:]
        first = foo.printable[:]
        foo.print_board()
    if turns > 2:
        second = first[:]
        first = foo.printable[:]
        foo.print_board()
        if check(foo.printable, second):
            os.system('cls' if os.name == 'nt' else 'clear')
            print "\nIterations: " + str(turns)
            exit()

    print "\nIterations: " + str(turns)
    foo.take_turn()
    time.sleep(.125)
    print "\n\n"
