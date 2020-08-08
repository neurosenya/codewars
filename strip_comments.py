'''
Strips all text that follows any of a set of comment markers passed in .
Any whitespace at the end of the line should also be stripped out.

1) Create a regex pattern that recognizes string with a character from 'markers'
   and everything till the nextline character '\n'
2) Substitute all regex patterns with just '\n'
3) Return the resulting string

Bugs:
1) Fix the problem with the last character, which is not always '\n'

.*? - non-greedy version of .*. it matches the least possible '.' in a string

(?=(\n | $)) - matches till the \n or $(end of the string).

(\r | \t | \f | \v)* - matches any whitespace, but a \n (newline)
'''

import re

def solution(string, markers):
    print(string+'\n' + 10*str('-'))
    for i in markers:
        comment = re.compile(rf'(\r|\t|\f|\v)*\{i}.*?(?=(\n|$))')
        matches = comment.findall(string)
        #print(matches)
        string  = re.sub(comment, '', string)
    spaces = r'(\r|\t|\f|\v)*'
    string = re.sub(spaces, '', string)
    return string

def solution2(string, markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas @apples", ["#", "@"]))
