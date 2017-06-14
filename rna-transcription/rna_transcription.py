def to_rna(dna, dna_nucl='ACGT', rna_nucl='UGCA', errors='XU'):
    for c in errors:
        if c in dna:
            return ''
    return dna.translate(str.maketrans(dna_nucl, rna_nucl))
