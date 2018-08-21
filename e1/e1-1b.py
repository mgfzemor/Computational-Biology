palindromes = {}

def read_file():
    sequence = ""
    file = open("file/sequence.fasta","r")
    file.readline()
    for line in file.readlines():
        sequence += line[:-1]
    return sequence

def output():
    del palindromes['NNNNNNNN']
    print("Palindromes of size 8 = {}".format(len(palindromes)))
    print("-----------------------------------------")
    for palindrome, count in palindromes.items():
        print("{} - {}".format(palindrome,count))

def generate_complement(sequence):
    complement = ""
    decode = {'A':'T','C':'G','G':'C','T':'A','N':'N'}
    for nucleotide in sequence:
        complement += decode[nucleotide]
    return complement

def reverse(sequence):
    return sequence[::-1]

def set_palindrome(sequence):
    global palindromes
    if sequence in palindromes:
        palindromes[sequence] += 1
    else:
        palindromes[sequence] = 1

def count_palindromes(sequence,size):
    limit = len(sequence) - size + 1
    for i in range(limit):
        subsequence = sequence[i:i+size]
        complementary_subsequence = generate_complement(subsequence)
        is_palindrome = reverse(subsequence) == complementary_subsequence
        if is_palindrome:
            set_palindrome(subsequence)

if __name__ == '__main__':
    sequence = read_file()
    count_palindromes(sequence,8)
    output()
