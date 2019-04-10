import itertools
import forward

'''
I	Q	If rotor steps from Q to R, the next rotor is advanced
II	E	If rotor steps from E to F, the next rotor is advanced
III	V	If rotor steps from V to W, the next rotor is advanced
IV	J	If rotor steps from J to K, the next rotor is advanced
V	Z	If rotor steps from Z to A, the next rotor is advanced

pick three in five
'''

'''
secretmessagesentheredatasecutiry

fsayuabiansukdnhbrqwwizqckivsdcxp
'''

'''
A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z

E	K	M	F	L	G	D	Q	V	Z	N	T	O	W	Y	H	X	U	S	P	A	I	B	R	C	J
A	J	D	K	S	I	R	U	X	B	L	H	W	T	M	C	Q	G	Z	N	P	Y	F	V	O	E
B	D	F	H	J	L	C	P	R	T	X	V	Z	N	Y	E	I	W	G	A	K	M	U	S	Q	O
E	S	O	V	P	Z	J	A	Y	Q	U	I	R	H	X	L	N	F	T	G	K	D	C	M	W	B
V	Z	B	R	G	I	T	Y	U	P	S	D	N	H	L	X	A	W	M	J	Q	O	F	E	C	K
'''

'''
ABCDEFGHIJKLMNOPQRSTUVWXYZ

YRUHQSLDPXNGOKMIEBFZCWVJAT
'''

rotorI = {}
rotorII = {}
rotorIII = {}
rotorIV = {}
rotorV = {}

rotors = []

rotorIAns = []
rotorIIAns = []
rotorIIIAns = []
rotorIVAns = []
rotorVAns = []

reverse = {}
reverseAns = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

ciph = "fsayuabiansukdnhbrqwwizqckivsdcxp"
msg = "secretmessagesentheredatasecutiry"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert(c, rotorA, rotorB, rotorC, rev_rotorA, rev_rotorB, rev_rotorC):
    fir = rotorA[c]
    sec = rotorB[fir]
    thi = rotorC[sec]
    rev = reverse[thi]
    r_thi = rev_rotorC[rev]
    r_sec = rev_rotorB[r_thi]
    r_thi = rev_rotorA[r_sec]
    return r_thi

def solve(rotorA, rotorB, rotorC, rev_rotorA, rev_rotorB, rev_rotorC, conditions):
    for i in range(26):
        temp = alphabet[i]
        for j in conditions:
            r = forward.forward(rotorA, step=j)
            ans = r[temp]
            temp = ans
            print(j)
        print(ans, alphabet[i])
        if ans == alphabet[i]:
            return True
    return False

def rotate(rotorA, rotorB, rotorC, rev_rotorA, rev_rotorB, rev_rotorC, indexA, indexB, indexC):
    tA = rotorA
    rotorA[alphabet[i]] = tA[alphabet[(i + 1) % 26]]
    return

def workout(indexs, conditions):
    first = rotors[int(indexs[0])]
    second = rotors[int(indexs[1])]
    third = rotors[int(indexs[2])]

    rev_first = rev_rotors[int(indexs[0])]
    rev_second = rev_rotors[int(indexs[1])]
    rev_third = rev_rotors[int(indexs[2])]

    rotorA = {}
    rotorB = {}
    rotorC = {}
    rev_rotorA = {}
    rev_rotorB = {}
    rev_rotorC = {}

    for indexA in range(26):
        for indexB in range(26):
            for indexC in range(26):
                for i in range(26):
                    rotorA[alphabet[i]] = first[alphabet[(i + indexA) % 26]]
                    rotorB[alphabet[i]] = second[alphabet[(i + indexB) % 26]]
                    rotorC[alphabet[i]] = third[alphabet[(i + indexC) % 26]]
                    rev_rotorA[alphabet[i]] = rev_first[alphabet[(i - indexA) % 26]]
                    rev_rotorB[alphabet[i]] = rev_second[alphabet[(i - indexA) % 26]]
                    rev_rotorC[alphabet[i]] = rev_third[alphabet[(i - indexA) % 26]]

                if solve(rotorA, rotorB, rotorC, rev_rotorA, rev_rotorB, rev_rotorC, conditions):
                    return True


if __name__ == "__main__":
    rotorIAns = "E	K	M	F	L	G	D	Q	V	Z	N	T	O	W	Y	H	X	U	S	P	A	I	B	R	C	J".split("\t")
    rotorIIAns = "A	J	D	K	S	I	R	U	X	B	L	H	W	T	M	C	Q	G	Z	N	P	Y	F	V	O	E".split("\t")
    rotorIIIAns = "B	D	F	H	J	L	C	P	R	T	X	V	Z	N	Y	E	I	W	G	A	K	M	U	S	Q	O".split("\t")
    rotorIVAns = "E	S	O	V	P	Z	J	A	Y	Q	U	I	R	H	X	L	N	F	T	G	K	D	C	M	W	B".split("\t")
    rotorVAns = "V	Z	B	R	G	I	T	Y	U	P	S	D	N	H	L	X	A	W	M	J	Q	O	F	E	C	K".split("\t")

    for i in range(26):
        rotorI[alphabet[i]] = rotorIAns[i]
        rotorII[alphabet[i]] = rotorIIAns[i]
        rotorIII[alphabet[i]] = rotorIIIAns[i]
        rotorIV[alphabet[i]] = rotorIVAns[i]
        rotorV[alphabet[i]] = rotorVAns[i]
        reverse[alphabet[i]] = reverseAns[i]

    rev_rotorI = {v : k for k, v in rotorI.items()}
    rev_rotorII = {v : k for k, v in rotorII.items()}
    rev_rotorIII = {v : k for k, v in rotorIII.items()}
    rev_rotorIV = {v : k for k, v in rotorIV.items()}
    rev_rotorV = {v : k for k, v in rotorV.items()}

    '''
    s,a,s 8, 10
    c,a,c 2, 24
    a,c,a 24, 2
    a,s,a 10, 8
    s,d,i,c,a,s 13, 21, 30, 2, 10
    d,i,c,a,s,d 21, 30, 2, 10, 13
    i,c,a,s,d,i 30, 2, 10, 13, 21
    '''

    # pick three in five
    rotors = [rotorI, rotorII, rotorIII, rotorIV, rotorV]
    rev_rotors = [rev_rotorI, rev_rotorII, rev_rotorIII, rev_rotorIV, rev_rotorV]
    for i in itertools.combinations("01234", 3):
        if workout(i, [8, 10]):
            print(i)
            

