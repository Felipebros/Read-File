#!/usr/bin/python3

import sys

def read_file(argv):
    with open(str(argv[1]), 'r') as file_contents:
        for line in file_contents:
            line = line.rstrip()
            print(line)

if __name__ == "__main__":
    read_file(sys.argv)
