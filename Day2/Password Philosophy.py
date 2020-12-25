
def check_count_in_range(password, letter, start, stop):
    return password.count(letter) >= start and password.count(letter) <= stop


def check_indexes(password, letter, start, stop):
    return (password[start] == letter or password[stop] == letter) and (password[start] != password[stop])


def PartOne():
    with open("input.txt", "r") as f:
        letters = [num.split(": ") for num in f]
        part1_tally = 0
        part2_tally = 0
        for policy, password in letters:
            print(policy, password)
            length, letter = policy.split(" ")
            start, stop = length.split("-")
            start, stop = int(start), int(stop)
            if password.count(letter) >= start and password.count(letter) <= stop:
                part1_tally+=1

            # part 1
            if check_count_in_range(password, letter, start, stop): part1_tally += 1

            # part 2
            if check_indexes(password, letter, start, stop): part2_tally += 1
        print("Part 1", part1_tally)
        print("Part 2", part2_tally)


# def PartTwo():
#     with open("input.txt", "r") as f:
#


PartOne()
# PartTwo()
