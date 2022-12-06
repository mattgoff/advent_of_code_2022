class SignalDecoder:

    def __init__(self, filename: str, distinct: int):
        self.file_data = None
        self.filename = filename
        self.marker = None
        self.distinct = distinct
        self.read_in()

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.readlines()[0]

    def parser1(self):
        for idx, char in enumerate(self.file_data):
            temp = self.file_data[idx:idx + self.distinct]
            if len(set(temp)) == self.distinct:
                self.marker = idx + self.distinct
                return


def main():
    sd = SignalDecoder("input_prod.txt", 14)
    sd.parser1()
    print(f"{sd.marker=}")


if __name__ == "__main__":
    main()

