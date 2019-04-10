import copy

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def forward(rotor, step=1):
    temp = copy.deepcopy(rotor)
    for i in range(26):
        temp[alphabet[i]] = rotor[alphabet[(i + step) % 26]]
    return temp
        

if __name__ == "__main__":
    rotorIAns = "E	K	M	F	L	G	D	Q	V	Z	N	T	O	W	Y	H	X	U	S	P	A	I	B	R	C	J".split("\t")
    rotorI = {}
    for i in range(26):
        rotorI[alphabet[i]] = rotorIAns[i]
    print(rotorI)
    print(forward(rotorI))