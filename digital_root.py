"""
https://www.codewars.com/kata/541c8630095125aba6000c00
https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/python

DESCRIPTION:
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
"""


def digital_root(n):
    """
    Calculate the recursive sum of all of the digits in a number
    :param int n: number to calculate the digital root of
    :return int: digital root of n
    """
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int, str(n))))
