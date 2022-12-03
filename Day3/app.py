import string


class RuckSack:

    def __init__(self, filename: str):
        self.file_data = None
        self.filename = filename
        self.priority_sum_1 = 0
        self.priority_sum_2 = 0
        self.read_in()

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.readlines()

    def parser1(self):
        for line in self.file_data:
            compartment_1, compartment_2 = line[:len(line)//2], line[len(line)//2:]
            common = list(set(compartment_1).intersection(compartment_2))[0]
            self.priority_sum_1 += self.get_priority(common)

    def parser2(self):
        for x in range(0, len(self.file_data), 3):
            s1 = set(self.file_data[x].rstrip("\n"))
            s2 = set(self.file_data[x + 1].rstrip("\n"))
            s3 = set(self.file_data[x + 2].rstrip("\n"))

            s1_s2 = s1.intersection(s2)
            common = list(s3.intersection(s1_s2))[0]
            self.priority_sum_2 += self.get_priority(common)

    @staticmethod
    def get_priority(letter):
        if letter.islower():
            return ord(letter) - 96
        else:
            return ord(letter) - 38


def main():
    rs1 = RuckSack("input_prod.txt")
    rs1.parser1()
    print(f"{rs1.priority_sum_1=}")
    rs1.parser2()
    print(f"{rs1.priority_sum_2=}")


if __name__ == "__main__":
    main()

