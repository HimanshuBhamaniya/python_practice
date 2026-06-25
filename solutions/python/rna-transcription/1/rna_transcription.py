'''This function returns a RNA strand based on the given DNA strand.  '''
def to_rna(dna_strand):
    '''Generate RNA strand based on the given DNA strand.
    parameter:
        dna_strand (str): This the given DNA strand of which transcribed RNA strand will be
                           generated.
    return:
        rna_strand (str): This is the generated RNA strand.'''
    rna_strand = ''
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            rna_strand += 'C'
        if nucleotide == 'C':
            rna_strand += 'G'
        if nucleotide == 'T':
            rna_strand += 'A'
        if nucleotide == 'A':
            rna_strand +='U'
    return rna_strand