nucleotides = ['ATGCCACTATGGTAG','ATGCCAACATGGATGCCCGATATGGATTGA','CCATT-AATGATCA-CAGTT']
nuc_counts = []

for base in range(len(nucleotides)):
    base_A = nucleotides[base].count("A")
    base_T = nucleotides[base].count("T")
    base_G = nucleotides[base].count("G")
    base_C = nucleotides[base].count("C")
    #Add the nucleotide counts
    nuc_counts.extend([base_A,base_T,base_C, base_G])
    
    print(base_A,base_C,base_G, base_T)
