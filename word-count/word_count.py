def word_count(phrase):
    word_count = {}
    words = ''.join(c if c.isalnum() else ' ' for c in phrase.lower())
    words = words.split()
    for word in words:
        word_count[word] = words.count(word)
    return word_count
