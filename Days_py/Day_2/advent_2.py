import pandas as pd
import sys

def check_safety(line):
    diffs = [line[i+1] - line[i] for i in range(len(line) - 1)]
    if (all(x < 0 and x in range(-3,0) for x in diffs) or
        all(x > 0 and x in range(1,4) for x in diffs)):
        return True
    else:
        return False

def compare_levels(puzzle_input):
    data = []
    with open(puzzle_input) as file:
        for line in file:
            entry = [int(x) for x in line.split()]
            data.append(entry)
    
    total = 0
    for line in data:
        if check_safety(line):
            total += 1
    
    return total  

def compare_levels_two(puzzle_input):
    data = []
    with open(puzzle_input) as file:
        for line in file:
            entry = [int(x) for x in line.split()]
            data.append(entry)
    
    total = 0
    for line in data:
        if check_safety(line):
            total += 1
        else:
            for i in range(len(line)):
                temp = line.copy()
                temp.pop(i)
                if check_safety(temp):
                    total += 1
                    break
    
    return total  

if __name__ == '__main__':
    puzzle_input = sys.argv[1]
    print(compare_levels(puzzle_input))
    print(compare_levels_two(puzzle_input))