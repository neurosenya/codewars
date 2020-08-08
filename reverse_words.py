def reverse_words(text):
    words = text.split()
    spaces = [text.count(i*" ") for i in range(10)]
    for i in spaces:
        if i == len(words)-1:
            sep = spaces.index(i) * str(" ")
    rev_words = [''.join(w[::-1]) for w in words]
    rev_text = sep.join(rev_words)

    return(rev_text)


print(reverse_words('stressed desserts'))

# clever implemantation!
def reverse_words2(str):
    return ' '.join(s[::-1] for s in str.split(' '))
# In this implementation we account for ONE space in str.split(' ') and
# other spaces if they are will be included in a splitted words. Therefore,
# there is no need to count spaces like I did it. =)

print(reverse_words2('stressed desserts'))
