def read_in():
    with open("./Day1/input_prod.txt", "r") as in_file:
        return in_file.readlines()


def parser(data):
    counter = 0
    totals = []
    for line in data:
        if line.strip("\n").isnumeric():
            counter += int(line)
        else:
            totals.append(counter)
            counter = 0
    return totals


def top_three(data):
    data.sort()
    return data[-1:-4:-1]


def main():
    data = read_in()
    totals = parser(data)
    three = top_three(totals)
    print(totals)
    print(f"Max = {max(totals)}")
    print(f"Top Three = {sum(three)}")


if __name__ == "__main__":
    main()
