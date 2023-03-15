#!/usr/bin/python3
def weight_average(my_list=[]):
    sco = 0
    wei = 0

    if my_list == []:
        return 0

    for i in range(len(my_list)):
        sco = sco + (my_list[i][0] * my_list[i][1])
        wei = wei + (my_list[i][1])

    tem = sco / wei

    return tem
