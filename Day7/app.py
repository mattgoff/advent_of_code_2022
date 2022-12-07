class DiskStructure:
    def __init__(self, filename: str):
        self.file_data = None
        self.filename = filename
        self.read_in()
        self.p1_ans = 0
        self.p2_ans = 0
        self.file_sizes = dict()

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.read().split("\n")

    def parser1(self):
        path = list()
        for line in self.file_data:
            commands = line.strip(" ").split(" ")
            if commands[1] == 'ls':
                continue

            if commands[1] == 'cd':
                if commands[2] == '..':
                    path.pop()
                else:
                    path.append(commands[2])
            else:
                if commands[0].isnumeric():
                    val = int(commands[0])
                    # print(path, val)
                    for i in range(len(path) + 1):
                        path_key = '/'.join(path[:i])
                        if path_key not in self.file_sizes:
                            self.file_sizes[path_key] = 0

                        self.file_sizes[path_key] += val

    def p1_get_ans(self):
        for key, val in self.file_sizes.items():
            if val <= 100000:
                self.p1_ans += val

    def p2_get_ans(self):
        needed_to_free = self.file_sizes['/'] - (70000000 - 30000000)

        current_best = float('inf')
        for key, val in self.file_sizes.items():
            if val >= needed_to_free:
                current_best = min(current_best, val)
                print(key, val)

        self.p2_ans = current_best


def main():
    disk = DiskStructure("input_prod.txt")
    disk.parser1()
    disk.p1_get_ans()
    print(f"{disk.p1_ans=}")
    disk.p2_get_ans()
    print(f"{disk.p2_ans=}")


if __name__ == "__main__":
    main()

