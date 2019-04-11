from rotor import *


class Enigma:
    def __init__(self, first: Rotor, second: Rotor, third: Rotor, reverse):
        self.first = first
        self.second = second
        self.third = third
        self.reverse = reverse
        self.plugs = {}
        for i in range(26):
            self.plugs[alphabet[i]] = alphabet[i]

    def exchange_plugs(self, characterA, characterB):
        self.plugs[characterA] = characterB
        self.plugs[characterB] = characterA

    def convert(self, message):
        final = ""
        for i in range(len(message)):
            passPlugs = self.plugs[message[i]]
            passFir = self.first.forward(step=i + 1)[passPlugs]
            stepTwo = self.first.check(i + 1)
            stepThi = self.second.check(stepTwo)
            passSec = self.second.forward(step=stepTwo)[passFir]
            passThi = self.third.forward(step=stepThi)[passSec]
            passRev = self.reverse[passThi]
            revThi = self.third.rev_forward(step=stepThi)[passRev]
            revSec = self.second.rev_forward(step=stepTwo)[revThi]
            revFir = self.first.rev_forward(step=i + 1)[revSec]
            final += self.plugs[revFir]
            # print(i, stepTwo, stepThi, self.plugs[revFir])
            # print(message[i], passPlugs, passFir, passSec, passThi, passRev, revThi, revSec, revFir)

        return final