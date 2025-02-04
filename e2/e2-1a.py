from numpy import *

matchScore = 5
mismatchScore = -3
gapScore = -4
d = gapScore

def create_matriz(rows, cols):
    F = zeros((rows,cols),int)
    return F

def S(ai, bi):
    if ai == bi:
        r = matchScore
    else:
        r = mismatchScore
    return r

def init_DP(F, rows, cols):
    for i in range(rows):
        F[i,0] = d*i
    for j in range(cols):
        F[0,j] = d*j

def compute_DP(F, A, B):
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            match = F[i-1,j-1] + S(A[i-1],B[j-1])
            delete = F[i-1, j] + d
            insert = F[i, j-1] + d
            F[i,j] = max(match, insert, delete)

def stackback(F, A, B):
    AlignmentA, AlignmentB = '', ''
    i = len(A)
    j = len(B)
    score = F[i,j]
    while (i >= 0 and j >= 0):
        if i == 0 and j == 0:
            break
        if (F[i,j] == F[i-1,j-1] + S(A[i-1], B[j-1])):
            AlignmentA = A[i-1] + AlignmentA
            AlignmentB = B[j-1] + AlignmentB
            i = i - 1
            j = j - 1
        elif (F[i,j] == F[i-1,j] + d):
            AlignmentA = A[i-1] + AlignmentA
            AlignmentB = "-" + AlignmentB
            i = i - 1
        else:
            AlignmentA = "-" + AlignmentA
            AlignmentB = B[j-1] + AlignmentB
            j = j - 1

    return score, AlignmentA, AlignmentB

def output(F, AlignmentA, AlignmentB, identity, score, sep):
    print(AlignmentA)
    print(sep)
    print(AlignmentB)
    print(F)
    print("Score => {}".format(score))
    print("Identity => {:.2f}".format(identity))

def compute_identity(seq1, seq2):
    matches = 0
    separator = ''
    for index in range(len(seq1)):
        if seq1[index] == seq2[index]:
            matches += 1
            separator += '|'
        else:
            separator += ' '
    identity = (float(matches)/float(len(seq1)))*100.0
    return separator, identity


def needleman_wunsch(A,B):
    rows = len(A)+1
    cols = len(B)+1
    F = create_matriz(rows, cols)
    init_DP(F, rows, cols)
    compute_DP(F, A, B)
    score, AlignmentA, AlignmentB = stackback(F, A, B)
    sep, identity = compute_identity(AlignmentA, AlignmentB)
    output(F, AlignmentA, AlignmentB, identity, score, sep)

if __name__ == '__main__':
    # Caso de Teste 01
    A = 'ALIGNMENT'
    B = 'LIGAMENT'

    # #Caso de Teste 02
    # A = 'ATCCGATGCG'
    # B = 'ACGCGCTGGGATCG'

    needleman_wunsch(A,B)
