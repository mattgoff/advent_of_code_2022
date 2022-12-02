"""
Notes
----------------------------------
Rock > Scissors
Scissors > Paper
Paper > Rock

A -> Rock
B -> Paper
C -> Scissors

X -> Rock -> 1pt
Y -> Paper -> 2pt
Z -> Scissors -> 3pt

lost = 0pt
draw = 3pt
win = 6pt

"""


class RPSClass:
    wld = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    results_p1 = {
        "A": 2,
        "B": 1,
        "C": 3,
        }

    results_p2 = {
        "X": {          # Loose
            "A": 3,     # "C",
            "B": 1,     # "A",
            "C": 2,     # "B"
              },
        "Z": {          # Win
            "A": 2,     # "B",
            "B": 3,     # "C",
            "C": 1,     # "A"
            },
        "Y": {          # Draw
            "A": 1,
            "B": 2,
            "C": 3,
        }
    }

    def __init__(self, filename: str):
        self.file_data = None
        self.filename = filename
        self.my_score = 0
        self.read_in()

    def read_in(self):
        with open(self.filename, "r") as in_file:
            self.file_data = in_file.readlines()

    def parser1(self):
        for line in self.file_data:
            his_hand, my_hand = line.rstrip("\n").split(" ")
            self.my_score += self.results_p1[his_hand] + self.wld[my_hand]

    def parser2(self):
        for line in self.file_data:
            his_hand, my_hand = line.rstrip("\n").split(" ")
            self.my_score += self.results_p2[my_hand][his_hand] + self.wld[my_hand]


def main():
    rps1 = RPSClass("input_test.txt")
    rps1.parser1()
    print(f"My Score = {rps1.my_score=}")
    rps2 = RPSClass("input_prod.txt")
    rps2.parser2()
    print(f"My Score = {rps2.my_score=}")


if __name__ == "__main__":
    main()

