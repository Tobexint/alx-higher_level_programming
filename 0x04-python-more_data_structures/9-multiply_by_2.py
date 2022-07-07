#!/usr/bin/python3
def multiply_by_2(my_dict):
    t_dict = my_dict.copy()
    for x in t_dict.keys():
        t_dict[x] *= 2
    return (t_dict)
