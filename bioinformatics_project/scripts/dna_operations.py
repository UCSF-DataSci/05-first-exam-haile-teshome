import sys

#Return compliment of DNA sequence[A : T, C : G, G : C, T : A]
def complement(sequence): 
    complement_map = str.maketrans('TGCAtgca', 'ACGTacgt')
    return sequence.translate(complement_map)


#Reverse the order of DNA sequence
def reverse(sequence):
    return sequence[::-1]

#Return the reverse complement of a DNA sequence
def reverse_complement(sequence):
    return reverse(complement(sequence))

if __name__ == "__main__":

    #Check number of arguements
    if len(sys.argv) != 2:
        print("Usage: python dna_operations.py <DNA sequence>")
        sys.exit(1)

    #Initiate the DNA sequence from command line arguement
    dna_sequence = sys.argv[1]

    #Calculate the complement, reverse and reverse complement of a DNA sequence
    dna_complement = complement(dna_sequence)
    dna_reverse = reverse(dna_sequence)
    dna_reverse_complement = reverse_complement(dna_sequence)

    #Print results
    print(f"Original sequence: {dna_sequence}")
    print(f"Complement: {dna_complement}")
    print(f"Reverse: {dna_reverse}")
    print(f"Reverse complement: {dna_reverse_complement}")
