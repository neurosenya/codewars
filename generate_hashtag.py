def generate_hashtag(s):
    if len(s) == 0:
        return False
    s = s.capitalize()
    l = [i.capitalize() for i in s.split()]
    res = '#' + ''.join(l)
    if len(res) <= 140:
        return res
    else:
        return 'False'

s = ""
print(generate_hashtag(s))
