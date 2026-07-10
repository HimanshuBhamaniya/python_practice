'''Function for finding proteins from a strand of codons.'''
def proteins(strand):
    '''Returns protein from a strand of codons.
    parameter:
        strand (str): Its the given strand of codons.
    return (list): It returns a list of amino acids that forms protein.'''
    codon_table = {
         'AUG': 'Methionine',
         'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
         'UUA': 'Leucine', 'UUG': 'Leucine',
         'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
         'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
         'UGU': 'Cysteine', 'UGC': 'Cysteine',
         'UGG': 'Tryptophan',
         'UAA': None, 'UAG': None, 'UGA': None
     }
    protein = []
    for split in range(0, len(strand), 3):
        codon = strand[split:split+3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid is None:
                break
            protein.append(amino_acid)
    return protein
