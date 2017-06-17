# from string import whitespace


def word_count(phrase):
    word_count = {}
    for word in phrase.lower().replace(',', ' ').replace('_', ' ').split():
        word = ''.join(filter(str.isalnum, word))
        if word and word not in word_count:
            word_count[word] = 1
        elif word:
            word_count[word] += 1
    return word_count
