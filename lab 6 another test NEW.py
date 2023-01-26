#lists
names = []
nucleotides = []
nuc_counts = []
total_mass = []
codons = []

#main
def main():
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")
    write_to_file()

def inputs(): #Get the file names
    file = input("Input file name? ")

    output = input("Output file name? ")
    
    return file, output


def write_to_file():
    
    #Get the file names
    filenames = inputs()
    
    file_input = filenames[0] #'dna.txt'
    file_output = filenames[1] #'hw-7-lab.txt'

    #open the files
    print(file_input)
    

def names_list():
    with open(myfile,"r") as file1:
        file1lines = file1.readlines()

        #names list
        names = file1lines[::2]
        
main()
