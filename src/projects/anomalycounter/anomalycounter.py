#!/usr/bin/env python3
"""
Anomaly counter
@author: Simon Parris
"""


def count(filename: str) -> int:
    """Count number of anomalies/blobs in an image"""
    fileFolder = "data/projects/anomalycounter/"
    f = open(fileFolder + "anomalycounter1.in", "r")
    readFile = f.readlines()
    myList = []
    for lines in readFile:
        myList.append(lines)
    print(myList)
    #raise NotImplementedError
def main():
    fileFolder = "data/projects/anomalycounter/"
    f = open(fileFolder + "anomalycounter1.in", "r")
    count(f)

if __name__ == "__main__":
    main()