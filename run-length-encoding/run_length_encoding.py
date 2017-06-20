def decode(line):
    cnt = ''
    decoded_line = ''
    for char in line:
        if char.isdigit():
            cnt += char
        else:
            decoded_line += ((char * int(cnt)) if cnt else char)
            cnt = ''
    return decoded_line


def encode(line):
    sym = []
    encoded_line = ''
    for char in line:
        if not sym or char not in sym[-1]:
            sym.append((char, 1))
        else:
            last = sym.pop(-1)
            sym.append((char, last[1] + 1))
    for char, cnt in sym:
        code = (char if cnt == 1 else str(cnt) + char)
        encoded_line += code
    return encoded_line
