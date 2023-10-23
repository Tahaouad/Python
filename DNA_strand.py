def DNA_strand(dna):
    translation_table = str.maketrans("T", "O")
    return dna.translate(translation_table)
print(DNA_strand('TAHA'))