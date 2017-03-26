import random
import Cell


class Board:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.board = {}
        self.random_fill_board()
        self.printable = []

    def print_board(self):
        self.printable = []
        for i in range(self.dimensions):
            temp = ""
            for j in range(self.dimensions):
                if self.board[str(i) + "," + str(j)].state:
                    temp += "X "
                else:
                    temp += ". "
            self.printable.append(temp)

    def print_printable(self):
        for line in self.printable:
            print line

    def random_fill_board(self):
        # __file = open('start.txt', 'a+')
        # __file.truncate()
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                num = random.randint(0,99)
                alive = False
                if num < 25:
                    alive = True
                key = str(i) + "," + str(j)
                self.board[key] = Cell.Cell(i, j, alive, self.dimensions)
                # to_write = str(i)+","
                # to_write += str(j)+","
                # to_write += str(alive)+","
                # to_write += str(self.dimensions)+"\n"
                # __file.write(to_write)

    def file_fill_board(self):
        __file = open('start.txt', 'r+')
        for line in __file:
            line = line.replace('\n', '')
            line = line.split(',')
            key = str(line[0])+","+str(line[1])
            i = int(line[0])
            j = int(line[1])
            alive = line[2] == 'True'
            dimensions = int(line[3])
            self.board[key] = Cell.Cell(i, j, alive, dimensions)


    def take_turn(self):
        for key, cell in self.board.iteritems():
            cell.count_neighbors(self.board)

        for key, cell in self.board.iteritems():
            cell.next_itteration()

        for key, cell in self.board.iteritems():
            cell.next_turn()
