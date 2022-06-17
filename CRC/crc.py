from random import randint, uniform


class CRC:
    def __init__(self, D, P):
        self.D = D
        self.P = P
        self.k = len(P)


    def getFCS(self) -> str:
        self.D += '0' * (self.k - 1)    # εισαγωγη των μηδενικων μετα το D

        copyOfD = self.D[:self.k]   # αρχικος υπολογισμος του διαιρετεου

        # συνάρτηση xor για δυο δυαδικούς αριθμούς ιδίου μήκους
        def XOR(a, b) -> str:
            ans = ""
            for i in range(1, len(b)):  # ξεκιναω απο το δεικτη 1, ε.ω. οι δυο αριθμοι να εχουν το ιδιο μηκος
                ans += str(int(a[i]) ^ int(b[i]))
            return ans

        i = self.k  # αρχικοποειτε με την θεση του τελευταιου ψηφιου του διαιρεταιου

        # υλοποιηση της αριθμητικής modulo-2
        while i < len(self.D):
            if copyOfD[0] == '0':   # για την περίπτωση που αριθμός ξεκίνα με 0
                copyOfD = XOR('0'*i, copyOfD)   # χρησιμοποίω διαιρέτη που να ειναι μόνο 0 (μηκους i)
            else:
                copyOfD = XOR(self.P, copyOfD)  # XOR
            copyOfD += self.D[i]    # κατεβαζω το επομενο ψηφιο του αριθμου στον διαιρετεο
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

    # δημιουργει τυχαια δεδομενα, δηλ. την ποσοτητα D (δυδαδικος αριθμος)
    def createData(self) -> str:
        D = ""
        for _ in range(self.k):
            D += str(randint(0, 1))
        return D

    # προσθετει στο D το FCS
    def encode(self) -> str:
        D = self.createData()
        fcs = CRC(D, self.P).getFCS()
        return D + fcs


class Receiver:
    def __init__(self, message, P):
        self.message = message
        self.P = P

    # εξεταζει εαν το μηνυμα επιστρεφει υπολοιπο ισο με 0, εαν ναι τοτε δεν εχει εντωπυσει καποια αλλοιωση
    # (ισως ομως εχει αλλοωθει το περιεχομενο) και επιστρεφεται η τιμη True
    def decode(self) -> bool:
        crc = CRC(self.message, self.P)
        if int(crc.getFCS()) == 0:
            return True
        return False


class Channel:
    def __init__(self, message, BER):
        self.message = message
        self.BER = BER

    # αλλοιωνει τα δεδομενα με καποια δωσμενη συχνοτητα (BER)
    def dataTransmission(self) -> str:
        msg = ""
        for i in range(len(self.message)):  # προσπελαση των bit του μηνυματος
            if uniform(0, 1) < self.BER:    # εαν η τυχαια δεκαδικη τιμη ειναι μικροτερη απο το BER, τοτε 1 -> 0 & 0-> 1
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
    N = 100000
    for i in range(N):
        senderMsg = Sender(20, "110101").encode()
        channelTransmittedMsg = Channel(senderMsg, 10 ** -3).dataTransmission()
        receipt = Receiver(channelTransmittedMsg, "110101").decode()
        statData.append(Data(senderMsg, channelTransmittedMsg, receipt))

    countChanged = 0    # πληθος αλλοιωμενων μηνυματων
    countDetected = 0   # πληθος αλλοιωμενων μηνυματων που βρηκε ο CRC

    for data in statData:
        changed = data.hasChanged()
        detected = not data.isDetected()
        if changed:
            countChanged += 1
            if detected:
                countDetected += 1
    
    print(countChanged, countDetected)

    transErrors = (countChanged * 100.0) / N    # ποσοστο αλλοιωμενων μηνυματων
    errorsDetected = (countDetected * 100.0) / N    # ποσοστο αλλοιωμενων μηνυματων που βρηκε ο CRC
    undetectedErrors = 0     # ποσοστο αλλοιωμενων μηνυματων που δεν βρηκε ο CRC
    if countChanged != 0:
        undetectedErrors = ((countChanged - countDetected) * 100.0) / countChanged

    print(transErrors, errorsDetected, undetectedErrors)
