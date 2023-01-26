#call the results of the function with the function() 
#lists
#names = []
nucleotides = []
nuc_counts = []
total_mass = []
codons = []

def main():
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")
    inputs()
    names()
    nucleotides()
    #protein_check()
    outputs()
    
def inputs(): #Gets user input for file + output
    
    #initializ globals
    global file
    global output
    
    file = input("Input file name? ")

    output = input("Output file name? ")

def names(): #Stores the names of the sequences in a list

    #initialize globals
    global names
    
    with open(file,"r") as file1:
        
        file1lines = file1.readlines()
        
        #names list
        names = file1lines[::2]
        
    
    return names

def nucleotides(): #Everything nucleotides, stored in a list
    
    #initialize globals
    global nucleotides
    global nuc_counts
    global total_mass
    
    with open(file,"r") as file1:
            
        file1lines = file1.readlines()

        #Store the nucleotides in a list
        nucleotides = file1lines[1::2]
        nucleotides = list(map(lambda dna: dna.upper(), nucleotides))

        #Count the bases
        for base in range(0,len(nucleotides)):
            #nucleotide count
            base_A = nucleotides[base].count("A")
            base_T = nucleotides[base].count("T")
            base_G = nucleotides[base].count("G")
            base_C = nucleotides[base].count("C")
            #Add the nucleotide counts
            nuc_counts.extend([base_A,base_T,base_G,base_C])
            
            #Get the total mass
            A_per = 
        
    return nucleotides, nuc_counts, total_mass

def outputs(): #Writes everything to the specified file
    
    with open(output,"w") as file2:
            #repeat this for as many names as there are
            for line in range(len(names)):
                file2.write(f"Region Name: {names[line]}")
                file2.write(f"Nucleotides: {nucleotides[line]}")
                file2.write(f"Nuc. Counts: {nuc_counts[line:line+4]}" + "\n")
                file2.write("\n")


main()

    
