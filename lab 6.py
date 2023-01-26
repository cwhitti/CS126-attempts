#Describle the program
print("This program reports information about DNA")
print("nucleotide sequences that may encode proteins.")

#Get the filenames
input_file = input("Input file name? ")
output_file = input("Output file name? ")

def main():
    write_to_file(input_file,output_file)

def write_to_file(input_file,output_file):

    #What are the names of the sequences?
    seq_names = names(input_file)
    #print(seq_names)
    
    #What are the nucleotides?
    total_nucleotides = nucleotides_and_counts(input_file)
    
    nucleotides_list = total_nucleotides[0]
    nuc_counts_list = total_nucleotides[1]
    #print(nuc_counts_list)

    #What is the total mass
    total_mass = mass(input_file)

    #What is the codons list?
    total_codons = codons(input_file)

    #is the sequence a protein?
    total_proteins = proteins(input_file)

    file1 = open(input_file, "r")

    print(nuc_counts_list)

    with open(output_file,"w") as file2:
            #repeat this for as many names as there are
            for line in range(len(seq_names)):
            
                file2.write(f"Region Name: {seq_names[line]}")
                file2.write(f"Nucleotides: {nucleotides_list[line]}")
                file2.write(f"Nuc. Counts: {nuc_counts_list[line]}" + "\n")
                #file2.write(f"Total Mass%: {nucleotides_list[line]}" + "\n")
                file2.write("\n")
                
    file1.close()
    file2.close()


def names(input_file): #Determine list of names

    #Set up the list of names
    names = []

    #Open the file and get some names baybee!!!
    with open(input_file,"r") as file1:

        file1_contents = file1.readlines()

        #names list
        names = file1_contents[::2]

    #######THIS IS WHAT THIS FUNCTION SPITS OUT!!######
    return names
    
def nucleotides_and_counts(input_file): #Determine list of nucleotides

    #Set up list of nucleotides
    nucleotides_content = []

    #Set up list of nucleotide counts
    nuc_counts = []
    nuc_count_sets = []

    with open(input_file,"r") as file1:

        file1_contents = file1.readlines()
        
        #Determine list of nucleotides
        nucleotide_content= file1_contents[1::2]
        
        #turn those lil nucleotides uppercase ~~~~~CHANGE THOUGH!!!~~~~~~~
        nucleotides = list(map(lambda dna: dna.upper(), nucleotide_content))

        #Determine nuc counts
        for base in range(0,len(nucleotides)):
            #nucleotide count
            base_A = nucleotides[base].count("A")
            base_T = nucleotides[base].count("T")
            base_G = nucleotides[base].count("G")
            base_C = nucleotides[base].count("C")
            
            #Add the nucleotide counts
            nuc_list = [base_A,base_C,base_G, base_T]
            nuc_counts.append(nuc_list)

    #######THIS IS WHAT THIS FUNCTION SPITS OUT!!######
    
    return nucleotides, nuc_counts

def mass(input_file):
    #Create the mass list
    mass = []

    #bring in the nucleotide counts list
    all_nucleotides = nucleotides_and_counts(input_file)

    #Our nucleotide count lists
    nuc_counts = all_nucleotides[1]
    #print(nuc_counts)
    
    #Our mass values
    base_percentages = []
    sum_totals = []
    masses = [135.128, 111.103, 151.128, 125.107]

    #######THIS IS WHAT THIS FUNCTION SPITS OUT!!######

    
def codons(input_file):
    print("CODONS!")

def proteins(input_file):
    print("PROTEINS!")





main()
