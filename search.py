from enigma import *

# bq cr di ej kw mt


def search(machine, _used):
    mapping = {}
    for i in range(int(len(_used) / 2)):
        mapping[_used[2 * i]] = _used[2 * i + 1]
        mapping[_used[2 * i + 1]] = _used[2 * i]
    for j in range(len(ciph)):
        if ciph[j] in mapping.keys():
            rev = mapping[ciph[j]]
            res = machine.convert_char(rev, j)
            print(res, msg[j])
            if res in mapping.keys():
                if mapping[res] != msg[j]:
                    print(1, mapping)
                    print(ciph[j], msg[j], rev, res)
                    return
            elif msg[j] in mapping.keys():
                if mapping[ciph[j]] != res:
                    print(2, mapping)
                    print(ciph[j], msg[j], rev, res)
                    return
            else:
                mapping[res] = msg[j]
                mapping[msg[j]] = res
        if j == len(ciph) - 1:
            print("SUCCESS")


if __name__ == "__main__":
    file = open("iRings.txt", "r")
    lines = file.readlines()
    cnt = 0
    for line in lines:
        line = line.split("\n")[0]
        rotorSelection = eval(line[:9])
        line = line[10:]
        rotorProb = [int(rotorSelection[0]), int(rotorSelection[1]), int(rotorSelection[2])]
        hmn = line.split(" ")
        h = int(hmn[0])
        m = int(hmn[1])
        n = int(hmn[2])
        rotorFir = Rotor(rotorProb[0], h, rotors[rotorProb[0]], rev_rotors[rotorProb[0]])
        rotorSec = Rotor(rotorProb[1], m, rotors[rotorProb[1]], rev_rotors[rotorProb[1]])
        rotorThi = Rotor(rotorProb[2], n, rotors[rotorProb[2]], rev_rotors[rotorProb[2]])

        enigma = Enigma(rotorFir, rotorSec, rotorThi, reverse)
        enigma.plugs[hmn[3]] = hmn[4]
        enigma.plugs[hmn[4]] = hmn[3]
        enigma.plugs[hmn[5]] = hmn[6]
        enigma.plugs[hmn[6]] = hmn[5]
        enigma.plugs[hmn[7]] = hmn[8]
        enigma.plugs[hmn[8]] = hmn[7]
        enigma.plugs[hmn[9]] = hmn[10]
        enigma.plugs[hmn[10]] = hmn[9]
        enigma.plugs[hmn[11]] = hmn[12]
        enigma.plugs[hmn[12]] = hmn[11]
        used = [hmn[3], hmn[4], hmn[5], hmn[6], hmn[7], hmn[8], hmn[9], hmn[10], hmn[11], hmn[12]]
        if hmn[11] == "D" and hmn[7] == "I":
            search(enigma, used)
            print(line)
    print(cnt)