#!/usr/bin/env python3
import sys

argc = len(sys.argv) - 1

print("{} argument{}{}".format(argc, 's' if argc != 1 else '', ':' if argc != 0 else '.'))

for i, arg in enumerate(sys.argv[1:], 1):
    print("{}: {}".format(i, arg))
