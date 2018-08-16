class Colour:
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   END = '\033[0m'

def read_file():
    sequence = ""
    file = open("file/sequence.fasta","r")
    file.readline()
    for line in file.readlines():
        sequence += line[:-1]
    return sequence

def output(subsequence,start,end,mutation,position, subseq):
    out = ("Subsequence = " + Colour.GREEN + subsequence[:position] + Colour.RED + subsequence[position] + Colour.GREEN + subsequence[position+1:] + Colour.END + "\n"
           "Location of subsequence in FASTA sequence = {}:{}\n"
           "Mutation = {} replaced by {} in position {}.".format(start,end, subseq[position], mutation, position))
    print(out)

def find_in_sequence(sequence, subsequence):
    found, limit = False, len(sequence) - len(subsequence) + 1
    for i in range(limit):
        if not found:
            snp = sequence[i:i+len(subsequence)]
            if count_diffs(snp, subsequence) == 1:
                found = True
                position_mutation = diff_position(snp,subsequence)
                mutation = snp[position_mutation]
                output(snp,i,i+len(subsequence),mutation,position_mutation,subsequence)
        else:
            break

def count_diffs(sequence01, sequence02):
    diff = 0
    for index in range(len(sequence01)):
        if sequence01[index] != sequence02[index]:
            diff += 1
    return diff

def diff_position(sequence01, sequence02):
    for index in range(len(sequence01)):
        if sequence01[index] != sequence02[index]:
            return index

if __name__ == "__main__":
    subsequence = 'CAGGAGATCTTCGTGGCCAC'
    sequence = read_file()
    find_in_sequence(sequence, subsequence)
