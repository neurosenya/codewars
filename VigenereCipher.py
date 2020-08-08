from itertools import cycle

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.shift_vals = [self.alphabet.index(l) for l in self.key]
    def encode(self, text):
        shifts = []
        # assign shift values for each letter in a text
        for shift_val, letter in zip(cycle(self.shift_vals), text):
            shifts.append((letter, shift_val))
        encryp_text = []
        length_alphabet = len(self.alphabet)
        for i in shifts:
            if i[0] in self.alphabet:
                try:
                    new_letter = self.alphabet[self.alphabet.index(i[0])+ i[1]]
                    encryp_text.append(new_letter)
                except IndexError:
                    new_shift_val = i[1] - (length_alphabet-1 - self.alphabet.index(i[0]))
                    new_letter = self.alphabet[new_shift_val-1]
                    encryp_text.append(new_letter)
            else:
                encryp_text.append(i[0])
        encryp_text = "".join(encryp_text)
        return encryp_text
    def decode(self, text):
        shifts = []
        # assign shift values for each letter in a text
        for shift_val, letter in zip(cycle(self.shift_vals), text):
            shifts.append((letter, shift_val))
        decryp_text = []
        length_alphabet = len(self.alphabet)
        for i in shifts:
            if i[0] in self.alphabet:
                try:
                    new_letter = self.alphabet[self.alphabet.index(i[0]) - i[1]]
                    decryp_text.append(new_letter)
                except IndexError:
                    new_letter = self.alphabet[-1-self.alpahbet.index(i[0])]
                    decryp_text.append(new_letter)
            else:
                decryp_text.append(i[0])
        decryp_text = "".join(decryp_text)
        return decryp_text
# alphabet, keyword, input string
abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
text='laxxhsj'
c = VigenereCipher(key, abc)
decrypted_msg =  c.decode(text)
print(decrypted_msg)
