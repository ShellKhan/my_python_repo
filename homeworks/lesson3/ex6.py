def int_func(word):
    return word.capitalize()

phrase = input('Vestibulum a phrase latine sine litteris: ').split(' ')
capitalize = []
for word in phrase:
    capitalize.append(int_func(word))
print(' '.join(capitalize) + '.')
