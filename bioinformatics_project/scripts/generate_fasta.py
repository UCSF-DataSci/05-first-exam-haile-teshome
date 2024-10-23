import random
import os
#Generates a random DNA sequence given length
def generate_random_dna(length):
    bases = ['T', 'G', 'C', 'A']  
    return ''.join(random.choice(bases) for _ in range(length))

#Formats the DNA sequence to have the specified number of base pairs per line
def format_fasta_sequence(sequence, line_length=80):
    return '\n'.join(sequence[i:i+line_length] for i in range(0, len(sequence), line_length))

#Write the DNA sequence to a file in FASTA format
def save_fasta_file(sequence, file_path):
    with open(file_path, 'w') as fasta_file: 
        fasta_file.write(sequence)

if __name__ == "__main__":
    #Generate a random DNA sequence of n (in this case 1M )base pairs and save to fasta format to have 80 base pairs per line
    dna_sequence = generate_random_dna(1000000)
    formatted_sequence = format_fasta_sequence(dna_sequence)
    project_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    file_path = os.path.join(project_dir, '..', 'data', 'random_sequence.fasta')  # Save file in data/ directory
    save_fasta_file(formatted_sequence, file_path)
    print(f"Random DNA sequence generated and saved to {file_path}")
