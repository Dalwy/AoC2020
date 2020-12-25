def PartOne():
    with open("input.txt", "r") as f:
        list = [int(x) for x in f]
        list.sort()
    for x in range(len(list)):
        for j in range(x + 1, len(list)):
            if (list[x] + list[j]) == 2020:
                print(list[x] * list[j])

def PartTwo():
    with open("input.txt", "r") as f:
        list = [int(x) for x in f]
        list.sort()
        for x in range(len(list)):
            for j in range(x + 1, len(list)):
                for y in range(j+1, len(list)):
                    if (list[x] + list[j] + list[y]) == 2020:
                        print(list[x] * list[j] * list[y])


PartOne()
PartTwo()
