def permutations(string):
    s = list(string)
    perm0 = []
    perm0.append(s)
    def perm_tree(perm, fix_idx, s):
        new_perm = []
        for s in perm:
            for i in range(fix_idx, len(s)):
                sc = s.copy()
                sc[fix_idx] = s[i]
                sc[i] = s[fix_idx]
                new_perm.append(sc)
        if fix_idx < len(s):
            return perm_tree(new_perm, fix_idx+1, s)
        else:
            perm = ["".join(i) for i in perm]
            perm = set(perm)
            return list(perm)

    return perm_tree(perm0, 0, s)
string = input()
perms = permutations(string)
print(perms)

