def is_isogram(word):
    symbols = list(filter(str.isalpha, word.lower()))
    return len(symbols) == len(set(symbols))
