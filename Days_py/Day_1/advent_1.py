import sys
import pandas as pd

def total_distance(puzzle_input):
    
    data = pd.read_table(puzzle_input, header = None, sep = '   ')
    
    s = sorted(data[:][0])
    t = sorted(data[:][1])
    
    l_s = len(s)
    l_t = len(t)
    
    res = []
    
    for i in range(min(l_s, l_t)):
        res.append(abs(s[i]-t[i]))
    
    if l_s > l_t:
        for i in range(l_t,l_s):
            res.append(s[i])
    
    elif l_s < l_t:
        for i in range(l_s,l_t):
            res.append(t[i])
    
    return sum(res)

def similarity_score(puzzle_input):
    data = pd.read_table(puzzle_input, header = None, sep = '   ')
    
    s = sorted(data[:][0])
    t = sorted(data[:][1])
    
    look_up = {}
    for num in t:
        if num in look_up.keys():
            look_up[num] += 1
        else:
            look_up[num] = 1

    res = 0
    for num in s:
        if num in look_up.keys():
            res = res + num * look_up[num]
    return res

if __name__ == "__main__":
    puzzle_input = sys.argv[1]
    print(total_distance(puzzle_input))
    print(similarity_score(puzzle_input))