import sys

def is_in_order(nums, rules_dict):
    for i in range(len(nums)):
        if nums[i] not in rules_dict.keys() and i != len(nums) - 1:
            return False
        if nums[i] in rules_dict.keys():
            for j in range(i + 1, len(nums)):
                if nums[j] not in rules_dict[nums[i]]:
                    return False
                if nums[j] in rules_dict.keys() and nums[i] in rules_dict[nums[j]]:
                    return False
    return True

def print_queue(puzzle_input):
    s = []

    with open('advent_5_input.txt') as f:
        for line in f:
            s.append(line.strip())
    sepearator = s.index("")

    rules = s[:sepearator]
    updates = s[sepearator+1:]

    rules_dict = {}
    for rule in rules:
        precedent, antecedent = rule.split("|")
        precedent, antecedent = int(precedent), int(antecedent)
        
        if precedent in rules_dict.keys():
            rules_dict[precedent].append(antecedent)
        else:
            rules_dict[precedent] = [antecedent]
            
    res = []
    for update in updates:
        nums = [int(item) for item in update.split(",")]
        if is_in_order(nums, rules_dict):
            res.append(nums)

    sum1 = 0
    for revision in res:
        sum1 += revision[len(revision)//2]
        
    res = []
    for update in updates:
        nums = [int(item) for item in update.split(",")]
        if not is_in_order(nums, rules_dict):
            res.append(nums)
    
    corrected_lists = []

    for nums in res:
        correct_list = []
        while len(correct_list) < len(nums):
            for i in range(len(nums)):
                loop_break = False
                if nums[i] in correct_list:
                    continue
                for j in range(len(nums)):
                    if nums[j] in correct_list:
                        continue
                    if i == j:
                        continue
                    if nums[i] in rules_dict.keys() and nums[j] in rules_dict[nums[i]] and nums[j] not in correct_list:
                        continue
                    else:
                        i += 1
                        break
                if j == len(nums) - 1:
                    correct_list.append(nums[i])
                    break
                    
        corrected_lists.append(correct_list)
    sum2 = 0
    for correction in corrected_lists:
        sum2 += correction[len(correction)//2]
    
    return (f"{sum1}, {sum2}")

if __name__ == "__main__":
    puzzle_input = sys.argv[1]
    print(print_queue(puzzle_input))