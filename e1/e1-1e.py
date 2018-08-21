def read_file():
    sequence = ""
    file = open("file/sequence.fasta","r")
    file.readline()
    for line in file.readlines():
        sequence += line[:-1]
    return sequence

def encode(number):
    dict = {'0':'A','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
    for digit in number:
        
if __name__ == '__main__':
    sequence = read_file()
