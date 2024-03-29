import copy
from utils import *

'''
I	Q	If rotor steps from Q to R, the next rotor is advanced
II	E	If rotor steps from E to F, the next rotor is advanced
III	V	If rotor steps from V to W, the next rotor is advanced
IV	J	If rotor steps from J to K, the next rotor is advanced
V	Z	If rotor steps from Z to A, the next rotor is advanced

pick three in five
'''

'''
A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z

E	K	M	F	L	G	D	Q	V	Z	N	T	O	W	Y	H	X	U	S	P	A	I	B	R	C	J
A	J	D	K	S	I	R	U	X	B	L	H	W	T	M	C	Q	G	Z	N	P	Y	F	V	O	E
B	D	F	H	J	L	C	P	R	T	X	V	Z	N	Y	E	I	W	G	A	K	M	U	S	Q	O
E	S	O	V	P	Z	J	A	Y	Q	U	I	R	H	X	L	N	F	T	G	K	D	C	M	W	B
V	Z	B	R	G	I	T	Y	U	P	S	D	N	H	L	X	A	W	M	J	Q	O	F	E	C	K
'''


class Rotor:
    def __init__(self, index, init, rotor, rev_rotor):
        self.index = index
        if index == 0:
            self.ultimate = "Q"
        elif index == 1:
            self.ultimate = "E"
        elif index == 2:
            self.ultimate = "V"
        elif index == 3:
            self.ultimate = "J"
        elif index == 4:
            self.ultimate = "Z"
        self.init = init
        self.rotor = rotor
        self.rev_rotor = rev_rotor

    def check(self, step):
        if self.index == 0:
            if self.init < ord("Q") - ord("A") + 1 and self.init + step > ord("Q") - ord("A"):
                return int((self.init + step - 16) / 26 + 1)
        elif self.index == 1:
            if self.init < 5 and self.init + step > 4:
                return int((self.init + step - 4) / 26 + 1)
        elif self.index == 2:
            if self.init < 22 and self.init + step > 21:
                return int((self.init + step - 21) / 26 + 1)
        elif self.index == 3:
            if self.init < 10 and self.init + step > 9:
                return int((self.init + step - 9) / 26 + 1)
        elif self.index == 4:
            if self.init < 25 and self.init + step > 24:
                return int((self.init + step - 24) / 26 + 1)
        return 0

    def forward(self, c, last=0, step=1):
        # print(self.init, c, alphabet[(ord(c) - ord("A") - last + self.init + step) % 26])
        return self.rotor[alphabet[(ord(c) - ord("A") - last + self.init + step) % 26]]

    def rev_forward(self, c, last=0, step=1):
        # print(c, alphabet[(ord(c) - ord("A") - last + self.init + step) % 26])
        return alphabet[(ord(self.rev_rotor[alphabet[(ord(c) - ord("A") - last + self.init + step) % 26]]) - ord("A")) % 26]

