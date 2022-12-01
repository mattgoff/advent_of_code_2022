class ElfClass:
    def __init__(self, filename):
        self.file_data = None
        self.filename = filename
        self.totals = list()
        self.read_in()
        self.parser()
        self.sorted_totals()

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.readlines()

    def parser(self):
        counter = 0
        for line in self.file_data:
            if line.strip("\n").isnumeric():
                counter += int(line)
            else:
                self.totals.append(counter)
                counter = 0

    def sorted_totals(self):
        self.totals.sort()

    def get_top_x(self, count):
        return sum(self.totals[-1:-count + -1:-1])


def main():
    elf = ElfClass("input_prod.txt")
    print(f"Max = {elf.get_top_x(1)}")
    print(f"Top Three = {elf.get_top_x(3)}")


if __name__ == "__main__":
    main()
