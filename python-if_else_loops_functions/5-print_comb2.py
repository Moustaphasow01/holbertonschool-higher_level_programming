#!/usr/bin/python3

for x in range(0,100):
    if (x!=100):
    print(" {:02d},".format(x),end="")
    elif(x==100):
    print(" {:02d}".format(x))
