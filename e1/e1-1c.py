import hashlib
subsequences = {}

def read_file():
    sequence = ""
    file = open("file/sequence.fasta","r")
    file.readline()
    for line in file.readlines():
        sequence += line[:-1]
    return sequence

def set_subsequence(sequence):
    global subsequences
    sequence =  hashlib.md5(sequence)
    if sequence in subsequences:
        subsequences[sequence] += 1
    else:
        subsequences[sequence] = 1

def count_subsequences(sequence,size):
    limit = len(sequence) - size + 1
    for i in range(0,limit):
        subsequence = sequence[i:i+size]
        set_subsequence(subsequence)

if __name__ == '__main__':
    sequence = read_file()
    count_subsequences(sequence,37)
    for sub, count in subsequences.items():
        print("{} => {}".format(sub,count))
