def diamond(n):
    if n == 1:
        return "*"
    if n == 0:
        return None
    else:
        diamond_string = ""
        ind = int((n-1)/2) + 1
        ast = -1
        while ast < n:
            ast += 2
            ind -= 1
            spaces = ind * " "
            diamond_string += spaces + ast*"*" + "\n"
        while ast >= 1:
            ast -= 2
            ind += 1
            spaces = ind * " "
            diamond_string += spaces + ast*"*" + "\n"

        print(diamond_string)
        return diamond_string

print(diamond(5))
