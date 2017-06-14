def to_rna(dna):
    errors = ['X', 'U', '']
    for c in dna:
        if c in errors:
            return ''
    return dna.translate(str.maketrans('ACGT', 'UGCA'))
