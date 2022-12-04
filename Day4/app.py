class RoomPairs:

    def __init__(self, filename: str):
        self.file_data = None
        self.filename = filename
        self.parser1_count = 0
        self.parser2_count = 0
        self.read_in()

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.readlines()

    def parser1(self):
        for line in self.file_data:
            elf1_list, elf2_list = self.get_rooms(line)
            overlap = all(i in elf1_list for i in elf2_list) or all(i in elf2_list for i in elf1_list)
            if overlap:
                self.parser1_count += 1

    def parser2(self):
        for line in self.file_data:
            elf1_list, elf2_list = self.get_rooms(line)
            overalap = any(i in elf1_list for i in elf2_list) or any(i in elf2_list for i in elf1_list)
            if overalap:
                self.parser2_count += 1

    @staticmethod
    def get_rooms(self, line):
        elf1, elf2 = line.strip("\n").split(",")
        elf1_list = list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1))
        elf2_list = list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1))
        return elf1_list, elf2_list


def main():
    rp1 = RoomPairs("input_prod.txt")
    rp1.parser1()
    print(f"{rp1.parser1_count=}")
    rp1.parser2()
    print(f"{rp1.parser2_count=}")


if __name__ == "__main__":
    main()

