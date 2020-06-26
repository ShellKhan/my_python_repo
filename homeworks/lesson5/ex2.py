with open('my_text2.txt') as my_file:
    words_count = []
    lines_count = 0
    for line in my_file:
        lines_count += 1
        if len(line):
            words_count.append(len(line.split(' ')))
        else:
            words_count.append(0)
    print(lines_count)
    print(words_count)
