#!/usr/bin/env python3
"""
Exam strategy
"""
import os
from collections import namedtuple
from typing import List, Tuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: List[Item]) -> List[int]:
    """
    General Knapsack solution.

    This function takes the knapsack capacity and the list of items (named tuples) to consider.
    The function returns a list of chosen indices.
    This function is optional but highly recommended.
    Use of the named tuple Item is optional but encouraged.
    """
    #for line in file.split('\n'):
    #all_items.append(items)
    #items = Item(0,items.weight)
    #n = len(items)
    #set initial value as 0.
    #all_items = []

    all_items = []
    with open("data/projects/exam_strategy/questions{1}.in") as f:
        for line in f.split('\n'):
             items = items(line.split(' ')[0], items.split(' ')[1])
             all_items.append(items)
             print(all_items)
   
    n = len(all_items)
    if capacity == 0 or n == 0:
        return 0
    else:
        m = [[0] * capacity]
        for i in range(all_items.weight):
            m[0,all_items.weight] == 0
            if all_items.weight[i] > all_items.weight:
                m[all_items.value, all_items.weight] == m[all_items.value-1, all_items.weight]
            else:
                m[all_items.value, all_items.weight] = max(m[all_items.value-1,all_items.weight], 
                m[all_items.value-1, all_items.weight - all_items.weight[i]] + all_items.value[i])
        return m[all_items.value, all_items.weight]

        for i in range(len(m)):
            
            pass




def pick_questions_to_answer(filename: str) -> Tuple[List[int], int]:
    """
    Main selection function

    This function takes file name as an argument.
    The function returns a tuple of two items: the list of chosen indices and total point value of all selected questions.
    """
    return index,total
    #raise NotImplementedError
    pass

def main():
    """Entry point"""
    for i in range(1, 6):
        filename = f"data/projects/exam_strategy/questions{i}.in"
        selection = pick_questions_to_answer(filename)
        print(
            f"Case {i}: Items {sorted(selection[0])} sum up to {selection[1]}"
        )

if __name__ == "__main__":
    main()
