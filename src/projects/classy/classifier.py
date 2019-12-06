#!/usr/bin/env python3
"""
A Classy Problem
"""

from typing import Dict, List


def classify(people: dict) -> List[str]:
    """
    Classify people
    
    Return the ordered (highest to lowest) list
    """
    raise NotImplementedError


def read_file(filename: str) -> Dict[str, str]:
    """
    Read data from the file into a dictionary

    Return the {person: class} mapping
    """
    person = {}
    f = open(filename)
    #value represents the class of the person.
    for line in f:
        (name, value) = line.strip().split(':')
        person[name] = value
    return person
    #raise NotImplementedError



def main():
    """Entry point"""
    people = read_file("data/projects/classy/classy01.txt")
    print(classify(people))


if __name__ == "__main__":
    main()
