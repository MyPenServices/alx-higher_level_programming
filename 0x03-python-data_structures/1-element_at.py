#!/usr/bin/python3

def element_at(my_list, idx):
    # handle when  index (idx) is negative
    # check whether idx is greater than or equal to no of elements
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
