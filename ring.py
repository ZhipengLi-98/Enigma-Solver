ciph = "fsayuabiansukdnhbrqwwizqckivsdcxp"
msg = "secretmessagesentheredatasecutiry"

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

if __name__ == "__main__":
    for i in range(len(msg)):
        if msg[i] in rings.keys():
            rings[msg[i]].append((ciph[i], i))
        else:
            rings[msg[i]] = [(ciph[i], i)]
        flag[msg[i]] = True
    print(rings)
