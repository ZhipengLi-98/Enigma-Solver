from enigma import *
import itertools

if __name__ == "__main__":

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
                        # output.write(str(rotorProb) + " " + str(h) + " " + str(m) + " " + str(n) + " " + str(j) + " " + "S\n")
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
                                output.write(str(rotorProb) + " " + str(h) + " " + str(m) + " " + str(n) + " " + str(j) + " " + "S\n")

    output.close()

    '''
    # index, next, init
    rotorFir = Rotor(0, 0, rotors[0], rev_rotors[0])
    rotorSec = Rotor(1, 0, rotors[1], rev_rotors[1])
    rotorThi = Rotor(2, 0, rotors[2], rev_rotors[2])

    enigma = Enigma(rotorFir, rotorSec, rotorThi, reverse)
    
    enigma.exchange_plugs("A", "D")
    enigma.exchange_plugs("E", "S")
    enigma.exchange_plugs("U", "Z")
    enigma.exchange_plugs("G", "F")
    enigma.exchange_plugs("L", "O")
    print(enigma.convert(msg))
    '''
