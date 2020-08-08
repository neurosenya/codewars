def wave(word):
    wave_order = []
    for i in range(len(word)):
       temp_word = list(word)
       temp_word[i] = temp_word[i].upper()
       wave_order.append("".join(temp_word))
    return wave_order
print(wave("gap"))
