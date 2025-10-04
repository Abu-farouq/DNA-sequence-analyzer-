import matplotlib.pyplot as plt
def read_sequence():
    seq = input("Enter or paste your DNA sequence: ").upper().replace(" ", "")
    return seq
#this is to ask the user to paste or type a DNA sequence.
def nucleotide_count(seq):
    counts = {base: seq.count(base) for base in "ATGC"}
    return counts
      #this is for counting A, T, G, and C.
def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)
 #To Calculate GC percentage.
def find_motif(seq, motif):
    motif = motif.upper()
    positions = []
    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i+len(motif)] == motif:
            positions.append(i + 1)
    return positions
 # To find where a motif occurs (1-indexed).
def plot_nucleotides(counts):
    plt.bar(counts.keys(), counts.values(), color=["royalblue", "mediumseagreen", "tomato", "slateblue"])
    plt.title("Nucleotide Frequency")
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()
   # And this is to plot nucleotide frequency as a bar chart.
def main():
    print("=== DNA Sequence Analyzer ===\n")
    seq = read_sequence()
    motif = input("Enter motif to search for (e.g. ATG): ").upper()
    counts = nucleotide_count(seq)
    gc = gc_content(seq)
    motif_positions = find_motif(seq, motif)

    print("\n--- Results ---")
    print(f"Sequence length: {len(seq)} bp")
    print(f"Nucleotide counts: {counts}")
    print(f"GC content: {gc}%")

    if motif_positions:
        print(f"Motif '{motif}' found at positions: {motif_positions}")
    else:
        print(f"Motif '{motif}' not found.")

    plot_nucleotides(counts)
    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()