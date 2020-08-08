def create_phone_number(n):
    return "(" + "".join(str(i) for i in n[:3]) + ")" + " " + "".join(str(i) for i in n[3:6]) + "-" + "".join(str(i) for i in n[6:])


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(n))


# Again impressive simple solution from codewars
def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number2(n))

# Usage of map! I know about this neat function, but I actually never use it
def create_phone_number3(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

print(create_phone_number3(n))
