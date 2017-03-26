class Cell:
    def __init__(self, x, y, living_or_dead, size):
        self.x = x
        self.y = y
        self.state = living_or_dead
        self.neighbors = []
        self.living_neighbors = 0
        self.size = size
        self.set_neighbors()
        self.next_state = False

    def set_neighbors(self):
        neighbor_start_x = self.x - 1
        neighbor_start_y = self.y - 1
        for i in range(3):
            for j in range(3):
                if neighbor_start_x < 0:
                    neighbor_start_x = self.size - 1
                elif neighbor_start_x == self.size:
                    neighbor_start_x = 0
                if neighbor_start_y < 0:
                    neighbor_start_y = self.size - 1
                elif neighbor_start_y == self.size:
                    neighbor_start_y = 0
                if (self.x, self.y) != (neighbor_start_x, neighbor_start_y):
                    self.neighbors.append(str(neighbor_start_x) + "," + str(neighbor_start_y))
                neighbor_start_x += 1
            neighbor_start_x = self.x - 1
            neighbor_start_y += 1

    def count_neighbors(self, board):
        for cell in self.neighbors:
            if board[cell].state:
                self.living_neighbors += 1

    def next_itteration(self):
        self.next_state = False
        if (self.living_neighbors == 2 or self.living_neighbors == 3) and self.state:
            self.next_state = True
        elif not self.state and self.living_neighbors == 3:
            self.next_state = True

    def next_turn(self):
        self.living_neighbors = 0
        self.state = self.next_state
        self.next_state = False
