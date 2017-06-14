def to_rna(dna):
    errors = ['X', 'U', '']
    rna = ''
    for c in dna:
        if c in errors:
            return ''
        if c == 'A':
            rna += 'U'
            continue
        if c == 'C':
            rna += 'G'
            continue
        if c == 'G':
            rna += 'C'
            continue
        if c == 'T':
            rna += 'A'
    return rna
