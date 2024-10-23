import sys
import os

#Read a FASTA file and returns the DNA sequence as a string
def read_fasta_file(file_path):
    sequence = []
    with open(file_path, 'r') as fasta_file:
        for line in fasta_file:
            if not line.startswith(">"):  
                sequence.append(line.strip())  # Delete whitespace
    return ''.join(sequence)

#Function to find cut site locations in a DNA sequence
def find_cut_sites(sequence, cut_site):
    cut_site_cleaned = cut_site.replace('|', '')  # Remove the | character 
    cut_site_length = len(cut_site_cleaned)
    positions = []
    start = 0
    while True:
        start = sequence.find(cut_site_cleaned, start)
        if start == -1:  # Iterate as long as occurance occurs
            break
        positions.append(start)
        start += cut_site_length 
    return positions

#Function to find pairs of cut sites that are between 80 and 120 kbp apart
def find_cut_site_pairs(positions):
    pairs = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distance = positions[j] - positions[i]
            if 80000 <= distance <= 120000:
                pairs.append((positions[i], positions[j]))
    return pairs

if __name__ == "__main__":
    #Check number of arguements
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <FASTA file path> <cut site sequence>")
        sys.exit(1)

    # Read the FASTA file and cut site sequence from the command line
    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]
    dna_sequence = read_fasta_file(fasta_file)

    #Find all occurrences of the cut site betwen 80-120 kbp
    cut_site_positions = find_cut_sites(dna_sequence, cut_site)
    cut_site_pairs = find_cut_site_pairs(cut_site_positions)

    print(f"Analyzing cut site: {cut_site.replace('|', '')}")
    print(f"Total cut sites found: {len(cut_site_positions)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")
    print("First 5 pairs:")
    for i, (pos1, pos2) in enumerate(cut_site_pairs[:5]):
        print(f"{i+1}. {pos1} - {pos2}")

    #Save the summary of results to a file
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    summary_file_path = os.path.join(script_dir, '..', 'results', 'cutsite_summary.txt')  # Relative path to results/ directory
    with open(summary_file_path, 'w') as summary_file:
        summary_file.write(f"Analyzing cut site: {cut_site.replace('|', '')}\n")
        summary_file.write(f"Total cut sites found: {len(cut_site_positions)}\n")
        summary_file.write(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        summary_file.write("First 5 pairs:\n")
        for i, (pos1, pos2) in enumerate(cut_site_pairs[:5]):
            summary_file.write(f"{i+1}. {pos1} - {pos2}\n")

    print(f"Results saved to {summary_file_path}")
