queens = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def checkDiagonal(row, column):
    for y in range(len(queens)):
        for x in range(len(queens[y])):
            if y + x == row + column or y-x == row-column:
                if queens[y][x] == 1:
                    return False
    return True

def checkHorizontal(row):
    for element in queens[row]:
        if element == 1:
            return False
    return True

def checkVertical(column):
    for row in queens:
        if row[column] == 1:
            return False
    return True



def canPlace(row, column):
    if checkHorizontal(row) and checkVertical(column) and checkDiagonal(row, column):
        return True
    return False


def solve(n = 0):
    if n == len(queens):
        print(queens)
        return True

    for row in range(len(queens)):
        for column in range(len(queens)):
            # print(row, column)
            if canPlace(row, column):
                queens[row][column] = 1
                if solve(n+1):
                    return True
                queens[row][column] = 0


solve()