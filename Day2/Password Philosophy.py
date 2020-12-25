def PartOne():
    with open("input.txt", "r") as f:
        letters = [num.split(": ") for num in f]
        count1 = 0
        count2 = 0
        for policy, password in letters:
            print(policy, password)
            length, letter = policy.split(" ")
            start, stop = length.split("-")
            start, stop = int(start), int(stop)
            if password.count(letter) >= start and password.count(letter) <= stop:
                count1+=1
            if (password[start] == letter or password[stop] == letter) and (password[start] != password[stop]):
                count2+=1
        print(count1)
        print(count2)


# def PartTwo():
#     with open("input.txt", "r") as f:
#


PartOne()
# PartTwo()
