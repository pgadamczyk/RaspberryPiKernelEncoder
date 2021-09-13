#! /usr/bin/python3

import encoders
import time

while True:
    [leftEnc,rightEnc] = encoders.readEncoders();
    print("%d,%d" % (leftEnc,rightEnc));
    time.sleep(.01);  


