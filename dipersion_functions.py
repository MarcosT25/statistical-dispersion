# @author: Marcos Takahashi
# @school: Universidade Estadual de Campinas

import math

def avg_func(list):
    avg = sum(list)/len(list)
    return avg

def var_func(list):
    list.sort()
    avg = avg_func(list)
    var = 0
    for n in list:
        var += (n - avg)*(n - avg)
    var /= (len(list) - 1)
    return var

def stdev_func(list):
    stdev = math.sqrt(var_func(list))
    return stdev

def coef_var_func(list):
    avg = avg_func(list)
    stdev = var_func(list)
    coef = stdev/avg
    return coef

def median_func(list):
    list.sort()
    if len(list)%2:
        median = list[int(len(list)/2)]
    else:
        median = (list[int(len(list)/2) - 1] + list[int(len(list)/2)]) / 2
    return median

def q_func(list, q): #being q 1 or 3 to the first and third quartile
    list.sort()
    size = int(len(list))
    if q == 1:
        quart = (list[int((size/4)-1)] + list[int((size/4))]) / 2
    if q == 3:
        quart = (list[int(3*(size/4)-1)] + list[int(3*(size/4))]) / 2
    return quart

#  List examples for testing

list_1 = [146, 125, 139, 132, 121, 135, 114, 130, 169, 103, 118, 114, 115, 126, 132, 90, 131, 125, 110, 132, 151, 104, 131, 112, 131, 132, 106, 103, 127, 120, 147, 113, 137, 108, 117, 112, 136, 109, 132, 119, 147, 120, 123, 94, 130, 108, 94, 123, 117, 142, 110, 124, 109, 132, 126, 98, 104, 125, 113, 127, 121, 134, 128, 147, 104, 122, 108, 98, 140, 143, 147, 136, 133, 141, 135, 131, 141, 124, 117, 124, 125, 142, 161, 150, 141, 133, 147, 140, 137, 121, 129, 119, 150, 114, 94, 106, 100, 156, 149, 133]

list_2 = [6.77, 9.69, 38.40, 48.71, 5.96, 9.61, 71, 50.81, 15.71, 24.01, 38.36, 54.38, 6.73, 82.13, 6.07, 22.41, 27.91, 11.68, 11.38, 6, 79.25, 31.46, 11.16, 18.86]

list_3 = [16.94, 47.43, 48.36, 6.11, 10.28, 46.21, 46.60, 23.27, 25.91, 8.61, 23.90, 57.22, 23.65, 11.74, 50.22, 6.72, 35.99, 58.32, 10.54, 23.03, 18.83, 20.89, 12.79, 37.59]

list_4 = [5.51, 40.09, 25.23, 127.50, 110.85, 51.72, 7.45, 8.19, 21.36, 56.28, 18.54, 40.82, 39.92, 5.81, 57.67, 30.23, 41.52, 10.16, 8.76, 5.56, 84.49, 19.52, 19.24, 10.89]

list_5 = [3.4, 5.2, 4.7, 6, 8.4, 9.3, 2.1, 4.8]

list_6 = [2, 5, 8, 10, 12, 15, 8, 5, 12]

print(median_func(list_5))