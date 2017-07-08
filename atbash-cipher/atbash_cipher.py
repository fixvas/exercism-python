from string import ascii_lowercase

CIPHER = 'zyxwvutsrqponmlkjihgfedcba'
TRANS_TABLE = str.maketrans(ascii_lowercase, CIPHER)


def encode(text, group=5):
    res = []
    line = [c for c in text.lower() if c.isalnum()]
    cnt = 0
    for char in line:
        res.append(char.translate(TRANS_TABLE))
        cnt += 1
        if cnt % group == 0:
            res.append(' ')
            cnt = 0
    return ''.join(res).rstrip()


def decode(text):
    res = []
    for char in text:
        if char.isalnum():
            res.append(char.translate(TRANS_TABLE))
    return ''.join(res)
