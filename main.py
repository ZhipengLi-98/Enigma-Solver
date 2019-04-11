from enigma import *

if __name__ == "__main__":
    # index, next, init
    rotorFir = Rotor(0, 1, 0, rotors[0], rev_rotors[0])
    rotorSec = Rotor(1, 2, 0, rotors[1], rev_rotors[1])
    rotorThi = Rotor(2, -1, 0, rotors[2], rev_rotors[2])

    enigma = Enigma(rotorFir, rotorSec, rotorThi, reverse)
    '''
    AD, ES, UZ, GF, LO
    '''
    enigma.exchange_plugs("A", "D")
    enigma.exchange_plugs("E", "S")
    enigma.exchange_plugs("U", "Z")
    enigma.exchange_plugs("G", "F")
    enigma.exchange_plugs("L", "O")
    print(enigma.convert(msg))
