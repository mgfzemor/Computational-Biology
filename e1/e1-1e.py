def read_file():
    sequence = ""
    file = open("file/sequence.fasta","r")
    file.readline()
    for line in file.readlines():
        sequence += line[:-1]
    return sequence

def generate_complement(sequence):
    complement = ""
    decode = {'A':'T','C':'G','G':'C','T':'A','N':'N'}
    for nucleotide in sequence:
        complement += decode[nucleotide]
    return complement

def generate_mutations(sequence,position):
    mutations = {}
    nucleotides = {'A':'A','C':'C','G':'G','T':'T'}
    del nucleotides[sequence[position-1]]
    for nucleotide in nucleotides:
        mutation = sequence[:position-1]+nucleotide+sequence[position:]
        mutations[mutation] = 0
    return mutations

def encode(number):
    enconded_number = ""
    dict = {'0':'A','1':'T','2':'G','3':'C','4':'C','5':'G','6':'T','7':'A','8':'A','9':'C'}
    for digit in number:
        enconded_number += dict[digit]
    return enconded_number

def count_subsequences(sequence, subsequences, size):
    limit = len(sequence) - size + 1
    for i in range(0,limit):
        subsequence = sequence[i:i+size]
        if subsequence in subsequences:
            subsequences[subsequence]+=1
    return subsequences

def output(sequences):
    for sequence, count in sequences.items():
        print("{} => {}".format(sequence,count))

if __name__ == '__main__':
    number = '00242319'
    size = len(number)
    sequences = {}
    encoded_number = encode(number)
    complement = generate_complement(encoded_number)
    sequences = generate_mutations(encoded_number,5)
    sequences[encoded_number] = 0
    sequences[complement] = 0
    sequence = read_file()
    sequences = count_subsequences(sequence, sequences, size);
    output(sequences)
