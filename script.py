import argparse


def intcomp(array):
    i = 0
    while array[i] != 99:
        a = array[array[i + 1]]
        b = array[array[i + 2]]
        array[array[i + 3]] = a + b if array[i] == 1 else a * b
        i = i + 4
    return array
