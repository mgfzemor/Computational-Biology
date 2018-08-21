nucleotides = {'A':0,'C':0,'G':0,'T':0}
unrecognized = {}

def read_file():
    sequence = ""
    file = open("file/sequence.fasta","r")
    file.readline()
    for line in file.readlines():
        sequence += line[:-1]
    return sequence

def output():
    for nucleotide, count in nucleotides.items():
        print("Nucleotide: {} => {}".format(nucleotide,count))
    print("----------------------------")
    print "New character found?",

    if unrecognized:
        print("YES")
        print("----------------------------")
        for char, count in unrecognized.items():
            print("Character: {} => {}".format(char,count))
    else:
        print("NO")
        print("----------------------------")

def count_nucleotides(sequence):
    for nucleotide in sequence:
        if nucleotide in nucleotides:
            nucleotides[nucleotide] +=1
        else:
            if nucleotide in unrecognized:
                unrecognized[nucleotide] +=1
            else:
                unrecognized[nucleotide] = 1

if __name__ == '__main__':
    sequence = read_file()
    count_nucleotides(sequence)
    output()
