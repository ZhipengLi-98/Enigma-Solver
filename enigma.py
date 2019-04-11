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
            passFir = self.first.forward(passPlugs, step=i + 1)
            stepTwo = self.first.check(i + 1)
            stepThi = self.second.check(stepTwo)
            passSec = self.second.forward(passFir, last=(self.first.init + i + 1) % 26, step=stepTwo, offset=i + 1)
            passThi = self.third.forward(passSec, last=self.second.init + stepTwo, step=stepThi, offset=stepTwo)
            passRev = self.reverse[alphabet[(ord(passThi) - ord("A") - self.third.init - stepThi) % 26]]
            revThi = self.third.rev_forward(passRev, step=stepThi)
            revSec = self.second.rev_forward(revThi, last=self.third.init + stepThi, step=stepTwo)
            revFir = self.first.rev_forward(revSec, last=self.second.init + stepTwo, step=i + 1, offset=stepTwo)
            final += self.plugs[alphabet[(ord(revFir) - ord("A") - self.first.init - i - 1) % 26]]
            print(i, stepTwo, stepThi, self.plugs[alphabet[(ord(revFir) - ord("A") - i - 1) % 26]])
            print(message[i], passPlugs, passFir, passSec, passThi, passRev, revThi, revSec, revFir)
            print(final)

        return final

    def convert_char(self, c, step):
        passPlugs = self.plugs[c]
        passFir = self.first.forward(passPlugs, step=step + 1)
        stepTwo = self.first.check(step + 1)
        stepThi = self.second.check(stepTwo)
        passSec = self.second.forward(passFir, last=(self.first.init + step + 1) % 26, step=stepTwo, offset=step + 1)
        passThi = self.third.forward(passSec, last=self.second.init + stepTwo, step=stepThi, offset=stepTwo)
        passRev = self.reverse[alphabet[(ord(passThi) - ord("A") - self.third.init - stepThi) % 26]]
        revThi = self.third.rev_forward(passRev, step=stepThi)
        revSec = self.second.rev_forward(revThi, last=self.third.init + stepThi, step=stepTwo)
        revFir = self.first.rev_forward(revSec, last=self.second.init + stepTwo, step=step + 1, offset=stepTwo)
        final = self.plugs[alphabet[(ord(revFir) - ord("A") - self.first.init - step - 1) % 26]]
        # print(i, stepTwo, stepThi, self.plugs[revFir])
        # print(message[i], passPlugs, passFir, passSec, passThi, passRev, revThi, revSec, revFir)

        return final