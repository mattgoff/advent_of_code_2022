class Rope:
    def __init__(self, filename: str):
        self.file_data = list()
        self.filename = filename
        self.read_in()
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
        self.moves = {
            "U": [0, 1],
            "D": [0, -1],
            "R": [1, 0],
            "L": [-1, 0],
        }
        self.tail_1_visited = set()
        self.tail_1_visited.add((self.tail_x, self.tail_y))
        self.knots = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
        ]
        self.tail_2_visited = set()
        self.tail_2_visited.add(tuple(self.knots[-1]))

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.read().strip().split("\n")

    def are_in_range(self):
        x_range = self.head_x - self.tail_x
        y_range = self.head_y - self.tail_y
        if abs(x_range) <= 1 and abs(y_range) <= 1:
            return True
        return False

    def move1(self, new_x, new_y):
        self.head_x += new_x
        self.head_y += new_y

        if not self.are_in_range():
            x_direction = 0
            y_direction = 0
            if self.head_x != self.tail_x:
                x_direction = (self.head_x - self.tail_x) / abs(self.head_x - self.tail_x)
            if self.head_y != self.tail_y:
                y_direction = (self.head_y - self.tail_y) / abs(self.head_y - self.tail_y)

            self.tail_x += x_direction
            self.tail_y += y_direction

    def move2(self, new_x, new_y):
        self.knots[0][0] += new_x
        self.knots[0][1] += new_y

        for i in range(1, 10):
            self.head_x, self.head_y = self.knots[i - 1]
            self.tail_x, self.tail_y = self.knots[i]

            if not self.are_in_range():
                x_direction = 0
                y_direction = 0
                if self.head_x != self.tail_x:
                    x_direction = (self.head_x - self.tail_x) / abs(self.head_x - self.tail_x)
                if self.head_y != self.tail_y:
                    y_direction = (self.head_y - self.tail_y) / abs(self.head_y - self.tail_y)

                self.tail_x += x_direction
                self.tail_y += y_direction

            self.knots[i] = [self.tail_x, self.tail_y]

    def run1(self):
        for move in self.file_data:
            m_dir, m_count = move.split(" ")
            m_count = int(m_count)
            dir_x, dir_y = self.moves[m_dir]
            for x in range(m_count):
                self.move1(dir_x, dir_y)
                self.tail_1_visited.add((self.tail_x, self.tail_y))

    def run2(self):
        for move in self.file_data:
            m_dir, m_count = move.split(" ")
            m_count = int(m_count)
            dir_x, dir_y = self.moves[m_dir]
            for x in range(m_count):
                self.move2(dir_x, dir_y)
                self.tail_2_visited.add(tuple(self.knots[-1]))


def main():
    rope = Rope("input_prod.txt")
    rope.run1()
    print(f"{len(rope.tail_1_visited)=}")
    rope.run2()
    print(f"{len(rope.tail_2_visited)=}")


if __name__ == "__main__":
    main()

