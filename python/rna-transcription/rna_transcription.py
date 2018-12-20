'''
#the process code
def to_rna(dna_strand):
    dnaToRnaMap = {'G':'C','C':'G','T':'A','A':'U'}
    rna = ''
    for dna_slice in dna_strand:
        rna+=dnaToRnaMap[dna_slice]
    return rna
'''
#more effective code using maketrans
def to_rna(dna_strand):
    transTable = str.maketrans("GCTA","CGAU")
    return dna_strand.translate(transTable) 