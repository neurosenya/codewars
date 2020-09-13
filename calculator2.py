import re

class Calculator:

    def iterate_matches(self, pattern, string):
        for match in re.finditer(pattern, string):
            num1, infix, num2 = float(match.group(1)), match.group(2), float(match.group(3))
            if infix == '+':
                operation = str(num1 + num2)
            elif infix == '-':
                operation = str(num1 - num2)
            elif infix == '*':
                operation = str(num1 * num2)
            elif infix == '/':
                operation = str(num1 / num2)
            string = string.replace(match.group(0), operation)
            return string

    def simplify_expr(self, string):
        '''Calculate expressions with standart operators
        '''
        while ' * ' in string or ' / ' in string:
            # Creating pattern that recognizes only + and -
            pattern = re.compile(r'([+-]?[0-9]*[.]?[0-9]+) (\*|/) ([+-]?([0-9]*[.])?[0-9]+|\([+-]?([0-9]*[.])?[0-9]+\))')
            string = Calculator().iterate_matches(pattern, string)
        while ' + ' in string or ' - ' in string:
            # Creating pattern that recognizes only * and /
            pattern = re.compile(r'([+-]?[0-9]*[.]?[0-9]+) (\+|-) ([+-]?([0-9]*[.])?[0-9]+|\([+-]?([0-9]*[.])?[0-9]+\))')
            string = Calculator().iterate_matches(pattern, string)

        return string

    # calculate expression inside parenthesis
    def parenthesis(self, string):
        '''Calculate recursivelu expression in the innermost parenthesis
        '''
        innermost_parenth = re.compile(r'\((\d|\+|-|\/|\*| |\.)*\)')
        while '(' in string:
            match = re.search(innermost_parenth, string).group(0)
            string = string.replace(match, Calculator().simplify_expr(match[1:-1]))
        return string

    def evaluate(self, string):
        string = Calculator().parenthesis(string)
        return Calculator().simplify_expr(string)


s = '2 / 2 + 3 * 4 - 6'
print(s)
print('---------------------------')
print(Calculator().evaluate(s))
