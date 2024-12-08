import pandas as pd
import sys

def compare_levels(puzzle_input):
    data_frame = pd.read_csv(puzzle_input, header = None, sep =' ')
    compare_reports = []
    
    for i in range(data_frame.shape[0]):
        queue = []
        for j in range(data_frame.shape[1]):
            queue.append(data_frame[j][i])
        
        compare_reports.append(queue)
    
    res = 0
    for report in compare_reports:
        if report[1] > report[0]:
            increasing = True
        elif report[1] < report[0]:
            increasing = False
        else:
            continue
        
        prev = None
        count = 0
        for num in report:
            if increasing and ((prev and num > prev and num - prev <= 3) or prev == None) or not increasing and ((prev and num < prev and prev - num <= 3) or prev == None):
                prev = num
                count += 1
            else:
                break
        if count == len(compare_reports[0]):
            res += 1
            
    return res

if __name__ == '__main__':
    puzzle_input = sys.argv[1]
    print(compare_levels(puzzle_input))