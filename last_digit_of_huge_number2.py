'''
Best solution to this kata on codewars.
Here I explain how I understand this solution.
First of all, in my implementation the main problem is
that last digits goes in cycle of 4 and in new 10 numbers
cycle layout over new 10 numbers changes and
I used indexing  (I had a list of all possible
last digits fir a given number and n % 4 corresponded to that index)
of order to understand what is the last digit. And in order to solve that
I have decided to track TWO last digits - second digit gives the
information about the layout of cycle in  10 numbers

But this algorithm takes into account whole number that is the result of x ** last_digit_of_previous_power_number
Numbers get big, but they can be handled, because powers always <=9.

We n % 4 and then add 4 because, for example, 24 % 4 = 0 but power x**0 will always equal 1 and this is not
what we need, therefore we can  add 4 and we will get 0 + 4 = 4. Which is exactly what we need, actually -
last digit of x*4 and x ** 1242441241523464 should be the same.  if 2 % 4 = 2 , 2 + 4 = 6, x ** 2 and x ** 6
will give the same last digit. 
'''
def last_digit(lst):
    n = 1
    for x in reversed(lst):
        print('x = %s, and n = %s' % (x, n))
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10

huge_number = [4, 3, 6]
# [6, 3, 4]
print(last_digit(huge_number))
