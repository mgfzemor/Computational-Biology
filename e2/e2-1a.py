sequence01 = 'VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKY'
sequence02 = 'VLSAADKTNVKAAWSKVGGHAGEYGAEALERMFLGFPTTKTYFPHFDLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSSVSTVLTSKYR'
# sequence01 = 'ACTGGGTCAAC'
# sequence02 = 'ATTGGCCAC'


def create_matriz(m, n):
    matriz = []
    for i in range(n+1):
        matriz.append([])
        for j in range(m+1):
            matriz[i].append('0')
    return matriz

def init_matriz(matriz, sequence01, sequence02):
    for i in range(2,len(sequence01)+1):
        matriz[0][i] = sequence01[i-1]
    for j in range(2,len(sequence02)+1):
        matriz[j][0] = sequence02[j-1]

def init_DP(matriz):
    val = 0
    for coluna in range(len(matriz[0])):
        matriz[0][coluna] = val
        val -=5
    val = 0
    for linha in range(len(matriz)):
        matriz[linha][0] = val
        val -=5

def define_scores():
    match = 5
    mismatch = -3
    gap = -4
    return match, mismatch, gap

def needleman_wunsch(seq1,seq2):
    m, n = len(seq1), len(seq2)
    match, mismatch, gap = define_scores()
    S = create_matriz(m,n)
    init_DP(S)
    for j in range(1,m+1):
        for i in range(1,n+1):
            op1 = S[i-1][j-1] + mismatch
            if (seq1[j-1] == seq2[i-1]):
                op1 = S[i-1][j-1] + match
            op2 = S[i][j-1] + gap
            op3 = S[i-1][j] + gap
            S[i][j] = max(op1,op2,op3)
    align1, align2 = stacktrace(S,seq1,seq2)
    print(align1)
    print(align2)
    return S


def stacktrace(S,seq1,seq2):
    m, n = len(seq1), len(seq2)
    align1 = seq1[m-1]
    align2 = seq2[n-1]
    while (m>1) and (n>1):
        score_diagonal = S[n-1][m-1]
        score_top = S[n-1][m]
        score_left = S[n][m-1]
        max_score = max(score_top, score_diagonal, score_left)
        if max_score == score_diagonal:
            align1 += seq1[m-2]
            align2 += seq2[n-2]
            m -= 1
            n -= 1
        elif max_score == score_left:
            align1 += seq1[m-2]
            align2 += '-'
            m -= 1
        else:
            align1 += '-'
            align2 += seq2[n-2]
            n -= 1

    return align1[::-1], align2[::-1]





if __name__ == '__main__':
    matriz = needleman_wunsch(sequence01, sequence02)
    for linha in matriz:
        for col in linha:
            print("{0: <3}".format(col), end=" ")
        print("\n")
