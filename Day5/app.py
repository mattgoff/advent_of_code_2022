class SupplyStack:

    def __init__(self, filename: str):
        self.file_data = None
        self.filename = filename
        self.moves_raw = list()
        self.stacks_raw = list()
        self.stacks = dict()
        self.moves = list()
        self.results = ""
        self.read_in()
        self.get_raw_data()
        self.parse_crane_data()
        self.parse_move_data()

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.readlines()

    def get_raw_data(self):
        moves_start = 0
        for idx, line in enumerate(self.file_data):
            temp_line = line.strip("\n")
            if len(temp_line) == 0:
                moves_start = idx + 1
                break
            self.stacks_raw.append(temp_line)
        for i in range(moves_start, len(self.file_data)):
            temp_line = self.file_data[i].strip("\n")
            self.moves_raw.append(temp_line)

    def parse_crane_data(self):
        temp_keys = list(map(int, list(self.stacks_raw[-1].replace(' ', ''))))
        for key in temp_keys:
            self.stacks[key] = list()
        for i in range(0, len(self.stacks_raw) - 1):
            data = list(self.stacks_raw[i])
            for idx, char in enumerate(data):
                if data[idx] in [" ", "[", "]"]:
                    continue
                else:
                    if idx == 1:
                        self.stacks[idx].insert(0, data[idx])
                    else:
                        self.stacks[idx // 4 + 1].insert(0, data[idx])

    def parse_move_data(self):
        for line in self.moves_raw:
            data = line.split(" ")
            data_pre = [data[1], data[3], data[5]]
            self.moves.append(list(map(int, data_pre)))

    def run_crane9000(self):
        for line in self.moves:
            for i in range(0, line[0]):
                pick_up = self.stacks[line[1]].pop()
                self.stacks[line[2]].append(pick_up)

    def get_status(self):
        answer = []
        for key, crate in self.stacks.items():
            answer.append(crate[-1])
        self.results = "".join(answer)

    def run_crane9001(self):
        for line in self.moves:
            pickup = self.stacks[line[1]][-1 * line[0]:]
            self.stacks[line[1]] = self.stacks[line[1]][0:len(self.stacks[line[1]]) - line[0]]
            self.stacks[line[2]] = self.stacks[line[2]] + pickup


def main():
    data_set = "input_prod.txt"
    stack9000 = SupplyStack(data_set)
    stack9000.run_crane9000()
    stack9000.get_status()

    stack9001 = SupplyStack(data_set)
    stack9001.run_crane9001()
    stack9001.get_status()

    print(f"{stack9000.results=}")
    print(f"{stack9001.results=}")


if __name__ == "__main__":
    main()

