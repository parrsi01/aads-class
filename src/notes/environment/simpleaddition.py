#!/usr/bin/env python3
# encoding: UTF-8

import sys

def addition(x: int, y: int):
    """Function to add two integers together"""
    a = x + y
    return a

def main(data):
    """Entry point for file"""
    data = '1.in.txt'
    for i in data:
        x = data.readline()
        y = data.readline()
    print(addition(x,y))
    

if __name__ == '__main__':
    main(sys.stdin)
