import sys

def mull_it_over(s):
    i = 0
    res = []
    
    while i in range(len(s)):
        num1 = None
        num2 = None
        
        #check mul(
        if s[i] != 'm' or s[i+1] != 'u' and s[i+2] != 'l' and s[i+3] != '(':
            i += 1
            continue
        else:
            i += 4
        
        #check num1
        if not s[i].isnumeric() and not num1:
            i += 1
            continue
        else:
            num1 = 0
            while s[i].isnumeric():
                num1 = num1 * 10 + int(s[i])
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
    
    return(sum(res))

if __name__ == "__main__":
    s = sys.argv[1]
    print(mull_it_over(s))
