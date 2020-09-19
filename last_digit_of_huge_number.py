'''
Last digit of a huge number.
For a given list [x1, x2, ..., xn] compute the last (decimal) digit of a x1^(x2^(x3^(... ^xn)))

Calculating the exact numbers itselg is out of question, because they could be very huge
We can do this knowing that when multiplying two numbers, their last digit is the result of single multiplication of two other digits
and is not summed with anything. And last digits of powers go in cycle for each 1-9 digit.
For exampple, for two we have:
    2^1 = ..2, 2^2 = ..4, 2^3 = ..8, 2^4 = ..6, and then cycles repeats
    2^5 = ..2, 2^6 = ..4, 2^7 = ..8, 2^8 = ..6.
As we can see, it is possible to determine last digit for a number d^n quite easily using modular arithmetic. Because we are using decimal arithmetic nowadays, we can identify
position of any number in the sequence [1, 2, 3, 4] and by this determine last digit
of d^n
'''
def last_digit(lst):
    if not lst:
        return 1
    if len(lst) == 1:
        return int( str(lst[0])[-1] )
    one_period_digits = set([0, 1, 5, 6])

    two_period_digits = {
            4: (6, 4),
            9: (1, 9)
                        }
    four_period_digits = {
            2: (6, 2, 4, 8),
            3: (1, 3, 9, 7),
            7: (1, 7, 9, 3),
            8: (6, 8, 4, 2)
                          }
    # This part extracts only the required part for further calculations
    # - 2 last digits
    lst = [str(i) for i in lst]
    lst = [int( str(i)[-2:] ) if len(i) > 1 else i for i in lst]
    # I need to upgrade this part in order to properly calculate
    # the last digit of a number to some power
    # for that I need to find the last TWO digits
    while len(lst) > 1:
        print(lst)
        power = int( lst.pop() )
        #number = int( str(lst.pop())[-1] )
        number = int( lst.pop() )
        new_power = number**power % 100
        lst.append(new_power)

    return int( str(lst[0])[-1] )


answer = last_digit([4, 3, 6])
print(answer)







