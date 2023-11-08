#!/usr/bin/env python3
def toint(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst


def permutation(lst, r):
    if r == 1:
        temp = []
        for i in lst:
            temp.append([i])
        return temp
    else:
        ret = []
        for i in range(0, len(lst)):
            x = lst[i]
            temp = []
            for j in range(0, len(lst)):
                if j != i:
                    temp.append(lst[j])
            p = permutation(temp, r - 1)
            for j in range(0, len(p)):
                p[j].insert(0, x)
                ret.append(p[j])
        return ret


def check(lst):
    for i in range(1, len(lst) - 1):
        x = lst[i]
        dx = 2 * x
        for j in range(0, i):
            if lst[j] < dx and dx - lst[j] < len(lst):
                n = dx - lst[j]

                found = False
                for k in range(0, i):
                    if lst[k] == n:
                        found = True
                if not found:
                    return False
        for j in range(i + 1, len(lst)):
            if lst[j] < dx and dx - lst[j] < len(lst):
                n = dx - lst[j]

                found = False
                for k in range(i + 1, len(lst)):
                    if lst[k] == n:
                        found = True
                if not found:
                    return False
    return True


def solve(lst):
    """while check(lst) != True:
        random.shuffle(lst)
        print(lst)
        print(check(lst))
        print()

    print(lst)"""
    newlst = permutation(lst, len(lst))
    cnt = 0
    for i in newlst:
        if check(i):
            # print(i)
            cnt = cnt + 1
    print("" + str(len(lst) - 1) + " : " + str(cnt))


filename = "test0.txt"
x = 5
lst = []
for i in range(x + 1):
    lst.append(i)
solve(lst)
"""with open(filename, 'r') as file:
    
    for line in file:
        num = line.strip().split()
        
        if len(num) == 1 :
            lst = []
            for i in range(int(num[0])+1):
                lst.append(i)
        else:
            lst = toint(num)
        solve(lst)
        
              
file.close()"""
