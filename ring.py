from utils import *

rings = {}
flag = {}

'''
s,a,s 8, 10
c,a,c 2, 24
a,c,a 24, 2
a,s,a 10, 8
s,d,i,c,a,s 13, 21, 30, 2, 10
d,i,c,a,s,d 21, 30, 2, 10, 13
i,c,a,s,d,i 30, 2, 10, 13, 21
'''


def dfs(nexts, goal, depth):
    if goal in nexts:
        print(goal, depth)
        return True
    for i in nexts:
        if depth == 0:
            for j in alphabet:
                flag[j] = True
        if i in mapping.keys() and flag[i]:
            flag[i] = False
            if dfs(mapping[i], goal, depth + 1):
                print(i, depth)
                if depth > 0:
                    return True


if __name__ == "__main__":
    mapping = {}
    for i in range(len(msg)):
        if msg[i] in mapping.keys() and ciph[i] not in mapping[msg[i]]:
            mapping[msg[i]].append(ciph[i])
        elif msg[i] not in mapping.keys():
            mapping[msg[i]] = [ciph[i]]

    flag = {}

    for i in mapping.keys():
        print(i)
        dfs(mapping[i], i, 0)
        print()
