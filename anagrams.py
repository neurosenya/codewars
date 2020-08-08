def anagrams(word, words):
    anagrams = []
    refs = {i:word.count(i) for i in word}
    for w in words:
        ws = {i:w.count(i) for i in w}
        if ws == refs:
            anagrams.append(w)
    return anagrams


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
