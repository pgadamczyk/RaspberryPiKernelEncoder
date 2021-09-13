#! /usr/bin/python3

f = open("/dev/encoder-driver",'rb');

def readEncoders():
    bytes = f.read(8);
    int1 = int.from_bytes(bytes[0:3],"little",signed=True)
    int2 = int.from_bytes(bytes[4:7],"little",signed=True)
    return [int1,int2]

def resetEncoders():
    f.write(' ');

[rightEnc, leftEnc] = readEncoders();

print("%d,%d" % (rightEnc, leftEnc));
