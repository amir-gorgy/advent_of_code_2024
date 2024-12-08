import sys
import ast

def total_distance(s,t):
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    
    l_s = len(s)
    l_t = len(t)
    
    res = []
    
    for i in range(min(l_s, l_t)):
        res.append(abs(s_sorted[i]-t_sorted[i]))
    
    if l_s > l_t:
        for i in range(l_t,l_s):
            res.append(s_sorted[i])
    
    elif l_t > l_s:
        for i in range(l_s,l_t):
            res.append(t_sorted[i])
    
    return sum(res)

if __name__ == "__main__":
    s = ast.literal_eval(sys.argv[1])
    t = ast.literal_eval(sys.argv[2])
    print(total_distance(s,t))