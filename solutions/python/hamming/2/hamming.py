'''This is a function to find the number of differences between to dna strands'''
def distance(strand_a, strand_b):
    '''Calculates the total number of differences between two DNA strands.
    parameter:
        strand_a (str): Its a string of a DNA strand.
        strand_b (str): Its a string of second DNA strand.
    return (int): It returns the total number of differences between two strands.'''
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    difference = 0
    for index, nucleotide in enumerate(strand_a):
        if nucleotide != strand_b[index]:
            difference += 1
    return difference
    
