import sys
import re

def mull_it_over(puzzle_input):
    s = []
    with open(puzzle_input) as file:
        for line in file:
            s.append(line)
    s = "".join(s)
    
    x = re.findall("(?<=mul\()\d+,\d+(?=\))",s)
    res = 0

    for call in x:
        nums = re.findall("\d+",call)
        res = res + int(nums[0]) * int(nums[1])
    
    return res

def mull_it_over_do_dont(puzzle_input):
    s = []
    with open(puzzle_input) as file:
        for line in file:
            s.append(line)
    s = "" .join(s)
    
    i = 0
    res = []
    do = True
    
    while i in range(len(s)):
        num1 = None
        num2 = None
        
        if do and s[i:i+7] != "don't()":
            # check mul(
            if s[i] != 'm' or s[i+1] != 'u' and s[i+2] != 'l' and s[i+3] != '(':
                i += 1
                continue
            else:
                i += 4
                
            # check num1
            if not s[i].isnumeric() and not num1:
                i += 1
                continue
            else:
                num1 = 0
                while s[i].isnumeric():
                    num1 = num1*10 + int(s[i])
                    i += 1
            
            # check argument seperator
            if s[i] != ',':
                i += 1
                continue
            else:
                i+=1
            
            # check num2
            if not s[i].isnumeric() and not num2:
                i += 1
                continue
            else:
                num2 = 0
                while s[i].isnumeric():
                    num2 = num2 * 10 + int(s[i])
                    i += 1
            
            # check closing bracket
            if s[i] != ')':
                i += 1
                continue
            else:
                res.append(num1 * num2)
                i += 1
        
        elif do and s[i:i+7] == "don't()":
            do = False
            i += 1
            continue
        
        elif not do and s[i:i+4] == "do()":
            do = True
            i += 1
            continue
        else:
            i += 1

    return sum(res)

if __name__ == "__main__":
    puzzle_input = sys.argv[1]
    print(mull_it_over(puzzle_input))
    print(mull_it_over_do_dont(puzzle_input))