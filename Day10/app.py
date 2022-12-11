class CRT:
    def __init__(self, filename: str):
        self.file_data = list()
        self.filename = filename
        self.read_in()
        self.p2_ans = None
        self.x = 1
        self.o = []

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.read().strip().split("\n")

    def run1(self):
        self.o.append(0)
        for item in self.file_data:
            if item == "noop":
                self.o.append(self.x)
            else:
                temp = int(item.split()[1])
                self.o.append(self.x)
                self.o.append(self.x)
                self.x += temp
        self.o.append(self.x)

    @property
    def p1_ans(self):
        return sum(x * y for x, y in list(enumerate(self.o))[20::40])

    def run2(self):
        for item in self.file_data:
            if item == "noop":
                self.o.append(self.x)
            else:
                temp = int(item.split()[1])
                self.o.append(self.x)
                self.o.append(self.x)
                self.x += temp

        for i in range(0, len(self.o), 40):
            for j in range(40):
                print("#" if abs(self.o[i + j] -j) <= 1 else " ", end="")
            print()
def main():
    crt = CRT("input_prod.txt")
    # crt.run1()
    # print(f"{crt.p1_ans=}")
    crt.run2()
    # print(f"{crt.p2_ans=}")


if __name__ == "__main__":
    main()

