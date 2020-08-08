# My disgusting solution
def duplicate_encode(word):
    word = word.lower()
    print(word)
    dict_count = {l : word.count(l) for l in list(word)}
    word = word.replace("(", "*(")
    word = word.replace(")", "*)")
    print(word)
    if ")" in dict_count:
        if dict_count[")"] == 1:
            word = word.replace("*)", "(")
        else:
            word = word.replace("*)", ")")
        del dict_count[")"]

    if "(" in dict_count:
        if dict_count["("] > 1:
            word = word.replace("*(", ")")
        else:
            word = word.replace("*(", "(")
        del dict_count["("]
    print(word)
    for k, v in dict_count.items():
        if v == 1:
            word = word.replace(k, "(")
        else:
            word = word.replace(k, ")")
    return word
print(duplicate_encode("em@RuGuvOS)G(keOyQbbF(RuRPO"))

# Convenient and clever solution from Codewars
def duplicate_encode2(word):
        return "".join(["(" if word.lower().count(c)==1 else ")" for c in word.lower()])

print(duplicate_encode2("em@RuGuvOS)G(keOyQbbF(RuRPO"))
