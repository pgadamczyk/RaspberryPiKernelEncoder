#! /usr/bin/python3

import encoders
import time

while True:
    [l,r] = encoders.readEncoders();
    print("%d,%d" % (l,r));
    time.sleep(.01);  


