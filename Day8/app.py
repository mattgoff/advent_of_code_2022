class Forest:
    def __init__(self, filename: str):
        self.file_data = list()
        self.filename = filename
        self.read_in()
        self.grid = dict()
        self.row_count = len(self.file_data)
        self.column_count = len(self.file_data[0])
        self.not_count = 0

    def read_in(self):
        with open(self.filename, "r") as in_file:
            temp = in_file.read().split("\n")
            for line in temp:
                self.file_data.append(list(map(int, list(line))))

    def parser1(self):
        for row in range(self.row_count):
            for col in range(self.column_count):
                if row == 0 or col == 0 or row == self.row_count - 1 or col == self.column_count - 1:
                    self.grid[(row, col)] = self.file_data[row][col]
                else:
                    self.explore1(row, col)

    def explore1(self, row, col):
        current_tree_height = self.file_data[row][col]

        trees_up_list = [self.file_data[x][col] for x in range(row)]
        trees_down_list = [self.file_data[x][col] for x in range(row + 1, self.row_count)]
        trees_left_list = [self.file_data[row][x] for x in range(col)]
        trees_right_list = [self.file_data[row][x] for x in range(col + 1, self.column_count)]

        viewable_up = all([x < current_tree_height for x in trees_up_list])
        viewable_down = all([x < current_tree_height for x in trees_down_list])
        viewable_left = all([x < current_tree_height for x in trees_left_list])
        viewable_right = all([x < current_tree_height for x in trees_right_list])

        if any([viewable_up, viewable_down, viewable_left, viewable_right]):
            self.grid[(row, col)] = self.file_data[row][col]
        else:
            self.grid[(row, col)] = "."
            self.not_count += 1

    def display_grid1(self):
        grid_keys = list(self.grid.keys())
        for i in range(0, len(grid_keys), self.column_count):
            data = list(map(str, [self.grid[grid_keys[x]] for x in range(i, i + self.column_count)]))
            print(data)

    @property
    def p1_get_ans(self):
        return len(self.grid) - self.not_count

    def parser2(self):
        for row in range(1, self.row_count - 1):
            for col in range(1, self.column_count - 1):
                self.explore2(row, col)

    def explore2(self, row, col):
        current_tree_height = self.file_data[row][col]

        trees_up_list = [self.file_data[x][col] for x in range(row)]
        trees_up_list.reverse()
        trees_down_list = [self.file_data[x][col] for x in range(row + 1, self.row_count)]
        trees_left_list = [self.file_data[row][x] for x in range(col)]
        trees_left_list.reverse()
        trees_right_list = [self.file_data[row][x] for x in range(col + 1, self.column_count)]

        for idx, val in enumerate(trees_up_list):
            if val >= current_tree_height or idx == len(trees_up_list) - 1:
                t_up_value = idx + 1
                break
            t_up_value = 1

        for idx, val in enumerate(trees_left_list):
            if val >= current_tree_height or idx == len(trees_left_list) - 1:
                t_left_value = idx + 1
                break
            t_left_value = 1

        for idx, val in enumerate(trees_down_list):
            if val >= current_tree_height or idx == len(trees_down_list) - 1:
                t_down_value = idx + 1
                break
            t_down_value = 1

        for idx, val in enumerate(trees_right_list):
            if val >= current_tree_height or idx == len(trees_right_list) - 1:
                t_right_value = idx + 1
                break
            t_right_value = 1

        self.grid[(row, col)] = t_up_value * t_down_value * t_left_value  * t_right_value

    def display_grid2(self):
        grid_keys = list(self.grid.keys())
        for i in range(0, len(grid_keys), self.row_count - 2):
            data = list(map(str, [self.grid[grid_keys[x]] for x in range(i, i + self.column_count - 2)]))
            print(data)

    @property
    def p2_get_ans(self):
        return max(self.grid.values())


def main():
    forest = Forest("input_prod.txt")
    forest.parser1()
    print(f"{forest.p1_get_ans=}")

    forest.parser2()
    print(f"{forest.p2_get_ans=}")


if __name__ == "__main__":
    main()

