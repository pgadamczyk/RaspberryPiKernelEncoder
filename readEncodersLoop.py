#! /usr/bin/python3

import encoders
import time

RESET_TIME_SEC = 10;
startTime = time.now()
while True:
    [l,r] = encoders.readEncoders();
    print("%d,%d" % (l,r));
    if (time.now() > startTime + RESET_TIME_SEC):
        encoders.resetEncoders();
        startTime = time.now();
    time.sleep(.01);  


