# A program for doing a binomial expansion
'''
algorithm for expansion
given (c1*a+c2*b)^n

ALGORITHM Finding binomial expansion
DONE
if expression starts with "-"
    c1 = -1
    a = rest of expression
DONE
if expression contains intergers and after them letters:
    c1 = all integers till the first  letter
    a = rest of expression
DONE
extract power too

DONE
function binterm(c1*a, pow):
    if c1*a is just integers:
        calculate a_term = (c1*a)^(pow)
    elif c1*a contains letters:
        if c1 > 1 and a is present:
            calculate c1_term = c1^(pow)
            a_term = c1_term + str(a^int(pow))
        elif c1 == 0:
            a_term = ''

if one of the expresions is just '0':
    return binterm(c1*a, pow)

answer = []
for i=0 to i=n:
    a_term = binterm(c1*a, pow=n-i):
    b_term = bintern(c2(b, pow=i)
    bincoef = n!/i!/(n-i)!
    if bincoef > 1:
        answer.append( bincoef + a_term + b_term )
    if bincoef == 1:
        answer.append( a_term + b_term )

concatanate string with '+" beetween elements of the list
if there is "+-" substitute it with just "-"
'''
import re
import math

def expand(string) -> str:
    # decompose string into two expressions
    a = re.search(re.compile(r'\(.*(\+|-)'), string).group(0)[1:-1]
    b = re.search(re.compile('(?<!\()(\+|-).*\)'), string).group(0)
    power = int(re.search(re.compile(r'\^\d*'), string).group(0)[1:])
    # Checks whether b has negative sign and saves it 
    if b[0] == '-':
        b = b[:-1]
    else:
        b = b[1:-1]
    # Now we need to split our expressions into coefficient and letter
    coef = re.compile(r'-?\d*')
    term = re.compile(r'[a-zA-Z]+')
    a_coef = re.search(coef, a).group(0)
    b_coef = re.search(coef, b).group(0)
    a_term = re.search(term, a)
    b_term = re.search(term, b)
    # Checking special cases when only free coefficient is present
    def special_cases(x_coef, x_term):
        if x_term:
            x_term = x_term.group(0)
        else:
            x_term = ''
        if not x_coef and not x_term:
            x_coef = 0
        elif x_coef == '':
            x_coef = 1
        elif x_coef == '-':
            x_coef = -1
        return int(x_coef), x_term
    a_coef, a_term = special_cases(a_coef, a_term)
    b_coef, b_term = special_cases(b_coef, b_term)
    print('a:',a_coef, a_term)
    print('b:', b_coef, b_term)
    def binom_term(x_coef, x_term, power):
        ''' Calculates binomials terms that goes after
        the binomial coefficient
        '''
        if x_term == '':
            if x_coef == 0:
                return '', 0
            return '', x_coef**power
        elif x_term != '':
            if power == 0:
                return '', 1
            elif power == 1 and abs(x_coef) > 1:
                return x_term, x_coef
            elif abs(x_coef) == 1:
                if power == 1:
                    return x_term, 1
                return x_term + '^' + str(power), 1
            elif abs(x_coef) > 1 or x_coef == -1:
                coef_pow = x_coef**power
                term_pow = str(x_term) + '^' + str(power)
                return term_pow, coef_pow
            elif abs(x_coef) == 0:
                return '', 0

    expansion = []
    for i in range(0, power+1):
        binom_coef = int(math.factorial(power) / (math.factorial(power-i) * math.factorial(i)))
        a, ac = binom_term(a_coef, a_term, power-i)
        b, bc = binom_term(b_coef, b_term, i)
        if bc or bc == 0:
            print('bc:', bc)
            binom_coef *= int(bc)
        if ac or ac == 0:
            binom_coef *= int(ac)
        binom_coef = str(binom_coef)
        if binom_coef == '1' and a != '' or b != '':
            binom_coef = ''
        print(binom_coef)
        expansion.append(binom_coef + a + b)
    # move the negative sign up to the front
    answ ='+'.join(expansion)
    answ = re.sub(re.compile(r'\+-'), '-', answ)
    answ = re.sub(re.compile(r'\*$'), '', answ)
    return answ

s = '(x-1)^2'
print(expand(s))































