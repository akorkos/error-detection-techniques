from random import randint, uniform


class CRC:
    def __init__(self, D, P):
        self.D = D
        self.P = P
        self.k = len(P)

    def getFCS(self) -> str:
        self.D += '0' * (self.k - 1)

        copyOfD = self.D[:self.k]

        def XOR(a, b) -> str:
            ans = ""
            for i in range(1, len(b)):
                ans += str(int(a[i]) ^ int(b[i]))
            return ans

        i = self.k

        while i < len(self.D):
            if copyOfD[0] == '0':
                copyOfD = XOR('0'*i, copyOfD)
            else:
                copyOfD = XOR(self.P, copyOfD)
            copyOfD += self.D[i]
            i += 1

        if copyOfD[0] == '0':
            copyOfD = XOR('0'*i, copyOfD)
        else:
            copyOfD = XOR(self.P, copyOfD)
        
        return copyOfD


class Sender:
    def __init__(self, k, P):
        self.k = k
        self.P = P

    def createData(self) -> str:
        D = ""
        for _ in range(self.k):
            D += str(randint(0, 1))
        return D

    def encode(self) -> str:
        D = self.createData()
        fcs = CRC(D, self.P).getFCS()
        return D + fcs


class Receiver:
    def __init__(self, message, P):
        self.message = message
        self.P = P

    def decode(self) -> bool:
        crc = CRC(self.message, self.P)
        if int(crc.getFCS()) == 0:
            return True
        return False


class Channel:
    def __init__(self, message, BER):
        self.message = message
        self.BER = BER

    def dataTransmission(self) -> str:
        msg = ""
        for i in range(len(self.message)):
            if uniform(0, 1) < self.BER:
                if self.message[i] == "0":
                    msg += "1"
                else:
                    msg += "0"
            else:
                msg += self.message[i]       
        return msg


class Data:
    def __init__(self, originalMsg, receivedMsg, receipt):
        self.originalMsg = originalMsg
        self.receivedMsg = receivedMsg
        self.receipt = receipt

    def hasChanged(self) -> bool:
        return self.originalMsg != self.receivedMsg

    def isDetected(self) -> bool:
        return self.receipt


if __name__ == "__main__": 
    statData = []
    N = 1000000
    for i in range(N):
        senderMsg = Sender(20, "110101").encode()
        channelTransmittedMsg = Channel(senderMsg, 10 ** -3).dataTransmission()
        receipt = Receiver(channelTransmittedMsg, "110101").decode()
        statData.append(Data(senderMsg, channelTransmittedMsg, receipt))

    countChanged = 0
    countDetected = 0

    for data in statData:
        changed = data.hasChanged()
        detected = not data.isDetected()
        if changed:
            countChanged += 1
            if detected:
                countDetected += 1
    
    print(countChanged, countDetected)

    transErrors = (countChanged * 100.0) / N
    errorsDetected = (countDetected * 100.0) / N
    undetectedErrors = ((countChanged - countDetected)*100.0) / countChanged

    print(transErrors, errorsDetected, undetectedErrors)
