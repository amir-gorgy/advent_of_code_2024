import sys

def ceres_search(puzzle_input):
    s = []
    with open('./advent_4_input.txt') as file:
        for line in file:
            s.append(line.strip())

    directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

    word = "XMAS"
    res = 0

    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 'X':
                for d in directions:
                    counter = 1
                    row, col = i, j
                    while counter < len(word):
                        row += d[0]
                        col += d[1]
                        if 0 <= row < len(s) and 0 <= col < len(s[i]) and s[row][col] == word[counter]:
                            counter += 1
                        else:
                            break
                    if counter == len(word):
                        res += 1

    return (f"Total occurrences: {res}")

def xmas_search(puzzle_input):
    s = []
    with open(puzzle_input) as file:
        for line in file:
            s.append(line.strip())
            
    word = "MAS"
    res = 0
    
    directions = [(1,1), (-1,1), (1,-1), (-1,-1)]
    
    def check_word(word, row, col, d):
        for k in range(len(word)):
            r = row + k * d[0]
            c = col + k * d[1]
            if not (0 <= r < len(s) and 0 <= c < len(s[0]) and s[r][c] == word[k]):
                return False
        return True
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 'M':
                if check_word(word, i, j, directions[0]) and check_word(word, i + 2, j, directions[1]):
                    res += 1
                if check_word(word, i, j, directions[0]) and check_word(word, i, j + 2, directions[2]):
                    res += 1
                if check_word(word, i, j, directions[2]) and check_word(word, i + 2, j, directions[3]):
                    res += 1
                if check_word(word, i, j, directions[1]) and check_word(word, i, j + 2, directions[3]):
                    res += 1

    return f"Total occurrences: {res}"



if __name__ == "__main__":
    puzzle_input = sys.argv[1]
    print(ceres_search(puzzle_input))
    print(xmas_search(puzzle_input))