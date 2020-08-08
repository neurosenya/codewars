# my disgusting solution
def valid_parentheses(string):
	l = list(string)
	for i in l:
		if i=="(":
			if l.count(")") > 0:
				for i in range(l.index(i) + 1, len(l)):
					if l[i] == ")":
						del l[i]
						break
			else:
				return False
			l.remove("(")
			return valid_parentheses(l)
	#print(l)
	if l.count(")") != l.count("("):
		print(l)
		return False
	else:
		return True

# Smart solution from codewars
def valid_parentheses2(string):
	cnt =0
	for char in string:
		if char == "(": cnt += 1
		if char == "(": cnt -= 1
	return True if cnt == 0 else False
print(valid_parentheses2("  ("))
