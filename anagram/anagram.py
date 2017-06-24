def detect_anagrams(word, candidates):
    anagram = []
    word = [c.lower() for c in word]
    for item in candidates:
        symb = [c.lower() for c in item]
        if symb != word and sorted(symb) == sorted(word):
                anagram.append(item)
    return anagram
