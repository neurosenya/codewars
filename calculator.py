'''
Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces
returns the value of that expression
Multiplications and divisions have higher priority and should be performed from left to right.
ALGORITHM
1) Startng from the start of the string find all the components that that have (:
    1.1. Recursively solve expression inside the paranthesis
2) If there  are no more paranthesis: iterate over string and find numbers between which there is * or /
    2.1 Calculate that expression
    2.2 Substitutr x * y or x / y with a new calculated value.
3) If there are no more * and / in the expression: the iterate over string and find numbers between which
there is + or -
    3.1 Calculate that expression
    3.2 Substitute x + y or x - y with a new calculated value
4) If everything is correct return the resulting value.
'''
import re

class Calculator:

    def simplify_expression(self, string, sym1, sym2):
        pattern = re.compile(r'\d+\.?\d* ({}|{}) \d+\.?\d*'.format(sym1, sym2))
        matches = re.finditer(pattern, string)
        for match in matches:
            match_expr = match.group(0)
            separated_expr = re.split(r'({}|{})'.format(sym1, sym2), match_expr)
            num1 = int(separated_expr[0]); num2 = int(separated_expr[2])
            infix = separated_expr[1]

            if infix == '*':
                match_expr = r'{} \* {}'.format(num1, num2)
                string = re.sub(match_expr, str(int(num1 * num2)), string)

            elif infix == '+':
                match_expr = r'{} \+ {}'.format(num1, num2)
                string = re.sub(match_expr, str(int(num1 + num2)), string)

            elif infix == '/':
                string = re.sub(match_expr, str(int(num1 / num2)), string)

            elif infix == '-':
                string = re.sub(match_expr, str(int(num1 - num2)), string)

            return string

    def parenthesis(self, string):
        parenthesis_pattern = re.compile(r'\((\d|\+|-|\/|\*| |\.)*\)')
        while '(' in string:
            match_parenth = re.search(parenthesis_pattern, string).group(0)
            string = string.replace( match_parenth, Calculator().calculate(match_parenth) )
            rm_parenth_around_num = re.compile(r'\(\d+\)')
            parenth_around_num = re.search(rm_parenth_around_num, string)
            string = re.sub(rm_parenth_around_num, parenth_around_num.group(0)[1:-1], string)
        return string

    def calculate(self, string):
        while '*' in string or '/' in string:
            string = Calculator().simplify_expression(string, sym1=r'\*', sym2=r'/')
        while '+' in string or '-' in string:
            string = Calculator().simplify_expression(string, sym1=r'\+', sym2=r'-')
        return string

    def evaluate(self, string):
        string = Calculator().parenthesis(string)
        return Calculator().calculate(string)

string = '(12 + (3 + (1 + 1))) * (6 + 7)' 
print('-------------------------')
print(Calculator().evaluate(string))
