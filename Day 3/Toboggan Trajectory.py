def PartOne():
    with open("input.txt", "r") as f:
        lines = [tree for tree in f]
        lines = [list(line.rstrip()) for line in lines]
        right = 3
        down = 1
        trees = 0
        while down < len(lines):
            if right > len(lines[down]) - 1:
                right = right % len(lines[down])
            if lines[down][right] == '#':
                trees += 1
            right += 3
            down += 1
        print(trees)

def PartTwo():
    with open("input.txt", "r") as f:
        lines = [tree for tree in f]
        lines = [list(line.rstrip()) for line in lines]
        trees = 0
        all_trees = 1
        rightlist =[1, 3, 5, 7, 1]
        downlist = [1, 1, 1, 1, 2]
        for (right, down) in zip(rightlist, downlist):
            x = right
            y = down
            trees = 0
            while y < len(lines):
                if x > len(lines[y]) - 1:
                    x = x % len(lines[y])
                if lines[y][x] == '#':
                    trees += 1
                x += right
                y += down
            all_trees *= trees
        print(all_trees)

PartOne()
PartTwo()
