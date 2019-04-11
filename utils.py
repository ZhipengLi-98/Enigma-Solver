alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ciph = "FSAVUABIANSUKDNHBRQWWIZQCKIVSDCXP"
msg = "SECRETMESSAGESENTHEREDATASECUTIRY"

reverseBoard = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

rotorIAns = "E	K	M	F	L	G	D	Q	V	Z	N	T	O	W	Y	H	X	U	S	P	A	I	B	R	C	J".split("\t")
rotorIIAns = "A	J	D	K	S	I	R	U	X	B	L	H	W	T	M	C	Q	G	Z	N	P	Y	F	V	O	E".split("\t")
rotorIIIAns = "B	D	F	H	J	L	C	P	R	T	X	V	Z	N	Y	E	I	W	G	A	K	M	U	S	Q	O".split("\t")
rotorIVAns = "E	S	O	V	P	Z	J	A	Y	Q	U	I	R	H	X	L	N	F	T	G	K	D	C	M	W	B".split("\t")
rotorVAns = "V	Z	B	R	G	I	T	Y	U	P	S	D	N	H	L	X	A	W	M	J	Q	O	F	E	C	K".split("\t")

rotorI = {}
rotorII = {}
rotorIII = {}
rotorIV = {}
rotorV = {}

rev_rotorI = {}
rev_rotorII = {}
rev_rotorIII = {}
rev_rotorIV = {}
rev_rotorV = {}

reverse = {}

for i in range(26):
    rotorI[alphabet[i]] = rotorIAns[i]
    rotorII[alphabet[i]] = rotorIIAns[i]
    rotorIII[alphabet[i]] = rotorIIIAns[i]
    rotorIV[alphabet[i]] = rotorIVAns[i]
    rotorV[alphabet[i]] = rotorVAns[i]
    reverse[alphabet[i]] = reverseBoard[i]

rev_rotorI = {v: k for k, v in rotorI.items()}
rev_rotorII = {v: k for k, v in rotorII.items()}
rev_rotorIII = {v: k for k, v in rotorIII.items()}
rev_rotorIV = {v: k for k, v in rotorIV.items()}
rev_rotorV = {v: k for k, v in rotorV.items()}

rotors = [rotorI, rotorII, rotorIII, rotorIV, rotorV]
rev_rotors = [rev_rotorI, rev_rotorII, rev_rotorIII, rev_rotorIV, rev_rotorV]
