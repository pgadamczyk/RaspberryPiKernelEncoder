#! /usr/bin/python3

f = open("/dev/encoder-driver",'rb');

def readEncoders():
    bytes = f.read(8);
    leftInt = int.from_bytes(bytes[0:3],"little",signed=True)
    rightInt = int.from_bytes(bytes[4:7],"little",signed=True)
    return [leftInt,rightInt]

[leftEnc, rightEnc] = readEncoders();

print("%d,%d" % (leftEnc, rightEnc));
