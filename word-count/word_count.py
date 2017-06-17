def word_count(phrase):
    word_count = {}
    words = ''.join([w if w.isalnum() else ' ' for w in phrase.lower()])
    words = words.split()
    for word in words:
        word_count[word] = words.count(word)
    return word_count
