"""
https://www.codewars.com/kata/next-bigger-number-with-the-same-digits
https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python

DESCRIPTION:
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
"""


def next_bigger(n):
    """
    Function that given an integer search for the next bigger integer that can be done with the number digits
    :param int n: initial number
    :return int: next bigger number 
    """
    digits = [int(digit) for digit in str(n)]

    # Check if already biggest number with sorted: sorted(iterable[, key][, reverse])
    if sorted(digits, reverse=True) == digits:
        return -1
    else:
        ascending_last = []
        next_d = 9
        # Go through the list from the end
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > digits[i - 1]:

                # d is pivot digit
                d = digits[i - 1]

                # right side of the pivot
                last_digits = digits[i:]

                # Search the next digit in the last_digits
                for a in last_digits:
                    if next_d >= a > d:
                        next_d = a

                # Remove the next_d (next pivot) from list and add previous pivot
                for b in last_digits:
                    if b == next_d:
                        last_digits.remove(b)
                        break
                last_digits.append(d)

                # Sort the last digit list in ascending order
                last_digits = sorted(last_digits)

                # Construct the number
                pivot_last_digits = [next_d] + last_digits

                if len(digits) == len(pivot_last_digits):
                    nbn = pivot_last_digits

                elif len(digits) == (len(pivot_last_digits)+1):
                    nbn = [digits[0]] + pivot_last_digits
                else:
                    c = len(digits) - len(pivot_last_digits)
                    nbn = digits[0:c] + pivot_last_digits

                return int("".join(map(str, nbn)))

# Test in codewars
print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(72531))
