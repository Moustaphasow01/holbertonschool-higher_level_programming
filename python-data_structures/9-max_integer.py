#!/usr/bin/python3
def max_integer(my_list=[]):
    max=0
    if (len(my_list)==0):
        return 'None'
    else:
        for x in range (len(my_list)):
            if(my_list[x]>max):
                max=my_list[x]

    return max
