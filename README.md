# Error detection techniques

This repository, includes two error detection methods more specifically 1-D, 2-D Parity Check and the Cyclic Redundancy Check (CRC) method. The material was developed, for the course [Digital Communications [NCO-04-05]](https://elearning.auth.gr/course/view.php?id=4101) (2021/22) of the Department of Computer Science at Aristotle University of Thessaloniki. 

## Description

The CRC implementation, is randomly generating k-bit binary messages in the transmitter (a block of k-bit data, where each bit has an equal probability of being 0 or 1). Then,calculates the CRC (FCS) corresponding to each message. A binary number, P, provided by the user, will be used as the standard for CRC calculation. Next, the message is transmitted and the CRC through a noisy channel with a Bit Error Rate (BER) and receiving the "corrupted" message at the receiver. Finally, the receiver is checking the CRC value.

For this particular assignment, the values used are $k=20, P=110101$, and $BER=10^{-3}$ and the follwing were calculated as well:

- the percentage of messages that arrive with errors (either in the data block or in the CRC) at the receiver,
- the percentage of messages that are falsely detected as erroneous by the CRC,
- the percentage of messages that arrive with errors at the receiver and are not detected by the CRC.

## Documentation

The results of the assignment are consolidated individually in their respective folders.
