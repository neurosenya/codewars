# Alphabetic anagrams
from collections import Counter
from math import factorial
from itertools import permutations
from math import floor

word ='BOOKKEEPER'
TotalUniquePermutations = factorial(len(word))
letters = Counter(word)
sorted_letter_counter = sorted([[key, value] for key, value in letters.items()], key=lambda x: x[0])

#wordPermutations = sorted(set(''.join(i) for i in permutations(word)))
#print(wordPermutations)
#print(sorted_letter_counter)
#print(wordPermutations)
start_num = 0
wordLength = len(word)
for i in range(0, len(word)):
    for m, let_count in enumerate(sorted_letter_counter):
        if word[i] == let_count[0]:
            LexicoPosLett = m
            break

    fact = factorial(wordLength - (i + 1))
    move_by = 0
    for j, el in enumerate(sorted_letter_counter[:LexicoPosLett]):
        additional_facts= [t[1] for t in sorted_letter_counter]
        additional_facts[j] -= 1
        fact = factorial(wordLength - (i +1))
        for add_fact in additional_facts:
            if add_fact:
                fact /= factorial(add_fact)
        move_by += fact
    start_num += move_by

    sorted_letter_counter[LexicoPosLett][1] -= 1
    if sorted_letter_counter[LexicoPosLett][1] == 0:
        del sorted_letter_counter[LexicoPosLett]

print(int(start_num+1))






















