user_var = input('Введите фразу: ')
user_words = user_var.split(' ')
for ind, word in enumerate(user_words, 1):
    print(ind, word[:10])