from enigma import *
import itertools


def searchS():
    cnt = 0
    output = open("sRings.txt", "w")
    for i in itertools.permutations([0, 1, 2, 3, 4], 3):
        rotorProb = list(i)
        # print(rotorProb)
        for h in range(26):
            for m in range(26):
                for n in range(26):
                    rotorFir = Rotor(rotorProb[0], h, rotors[rotorProb[0]], rev_rotors[rotorProb[0]])
                    rotorSec = Rotor(rotorProb[1], m, rotors[rotorProb[1]], rev_rotors[rotorProb[1]])
                    rotorThi = Rotor(rotorProb[2], n, rotors[rotorProb[2]], rev_rotors[rotorProb[2]])

                    prob = Enigma(rotorFir, rotorSec, rotorThi, reverse)
                    for j in alphabet:
                        cnt += 1
                        if cnt % 10000 == 0:
                            print(cnt * 100 / 27418560)
                        ans = copy.deepcopy(j)
                        tempA = prob.convert_char(ans, 8)
                        tempB = prob.convert_char(tempA, 10)
                        # print(tempA, tempB, ans)
                        if tempB == ans:
                            ttempA = prob.convert_char(ans, 13)
                            ttempB = prob.convert_char(ttempA, 21)
                            ttempC = prob.convert_char(ttempB, 30)
                            ttempD = prob.convert_char(ttempC, 2)
                            ttempE = prob.convert_char(ttempD, 10)
                            # print(ans, ttempA, ttempB, ttempC, ttempD, ttempE)
                            if ttempE == ans:
                                # print(rotorProb, h, m, n)
                                output.write(str(rotorProb) + " " + str(h) + " " + str(m) + " " + str(n) + " " + str(\
                                    j) + " " + "S\n")

    output.close()


def test():
    # index, init
    rotorFir = Rotor(2, 11, rotors[2], rev_rotors[2])
    rotorSec = Rotor(0, 17, rotors[0], rev_rotors[0])
    rotorThi = Rotor(3, 1, rotors[3], rev_rotors[3])

    enigma = Enigma(rotorFir, rotorSec, rotorThi, reverse)
    '''
    enigma.exchange_plugs("A", "D")
    enigma.exchange_plugs("E", "S")
    enigma.exchange_plugs("U", "Z")
    enigma.exchange_plugs("G", "F")
    enigma.exchange_plugs("L", "O")
    '''
    print(enigma.convert(ciph))


if __name__ == "__main__":
    # test()
    # searchS()

    aFile = open("aRings.txt", "r")
    iFile = open("iRings.txt", "w")
    sRings = aFile.readlines()
    cnt = 0
    for line in sRings:
        s = line.split("\n")[0]
        rotorSelection = eval(s[:9])
        s = s[10:]
        rotorProb = [int(rotorSelection[0]), int(rotorSelection[1]), int(rotorSelection[2])]
        hmn = s.split(" ")
        used = [hmn[3], hmn[4], hmn[5], hmn[6], hmn[7], hmn[8], hmn[9], hmn[10]]
        h = int(hmn[0])
        m = int(hmn[1])
        n = int(hmn[2])
        rotorFir = Rotor(rotorProb[0], h, rotors[rotorProb[0]], rev_rotors[rotorProb[0]])
        rotorSec = Rotor(rotorProb[1], m, rotors[rotorProb[1]], rev_rotors[rotorProb[1]])
        rotorThi = Rotor(rotorProb[2], n, rotors[rotorProb[2]], rev_rotors[rotorProb[2]])

        prob = Enigma(rotorFir, rotorSec, rotorThi, reverse)
        for j in alphabet:
            if j == "D":
                cnt += 1
                if cnt % 10000 == 0:
                    print(cnt * 100 / 27418560)
                ans = copy.deepcopy(j)
                tempA = prob.convert_char(ans, 30)
                tempB = prob.convert_char(tempA, 2)
                tempC = prob.convert_char(tempB, 10)
                tempD = prob.convert_char(tempC, 13)
                tempE = prob.convert_char(tempD, 21)
                if tempE == ans:
                    iFile.write(str(rotorProb) + " " + str(h) + " " + str(m) + " " + str(n) + " " + used[0] + " " + used[1]\
                              + " " + used[2] + " " + used[3] + " " + used[4] + " " + used[5]\
                                + " " + used[6] + " " + used[7] + " " + str(j) + " " + "I\n")
    iFile.close()
    aFile.close()


