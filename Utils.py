import Data

#convert an hexadecimal number to binary nember
def hexToBinary(nb):
    nb = nb.replace(" ", "").strip()
    nb = nb.zfill(16)
    binary = ""
    for i in nb:
        binary += bin(int(i,16)).zfill(6).replace("0b", "")
    return binary

# permutation of the key by IP
def permutationIP(nb):
    res = ""
    for i in range(0,64):
        res += nb[Data.IP[i] - 1]
    return res

# permutation of the key by IP_Inverse
def permutationIPInverse(nb):
    res = ""
    for i in range(0,64):
        res += nb[Data.IP_INVERSE[i] - 1]
    return res

# expansion Right of the key
def expension(rightkey):
    res = ""
    for i in range(0,48):
        res += rightkey[Data.EXPANSIONTABLE[i] - 1]
    return res
    

#  calculate xor
def xor(a, b):
    if len(a) != len(b):
        exit("La longueur de deux nombres doit etre la meme !!")

    res = ""
    for bit_a, bit_b in zip(a, b):
        res += str((int(bit_a) + int(bit_b)) % 2) 
    return res


# permutation the key of 64 bits to the key of 56 bits by PC1
def key64to56(key):
    res = ''
    for i in range(0,56):
        res += key[Data.PC1[i] - 1]
    return res


# permutation the key of 56 bits to the key of 64 bits
def key56to64(key):
    tmp = [2 for i in range(64)]                # cherche l'importance de 2
    for i in range(len(Data.PC1)):
        tmp[Data.PC1[i] - 1] = key[i]
    res = ""
    for i in tmp:
        res += str(i)
    return res  

# permutation the key of 56 bits to the key of 48 bits by PC2
def key56to48(key):
    res = ''
    for i in range(0,48):
        res += key[Data.PC2[i] - 1]
    return res

# permutation the key of 48 bits to the key of 56 bits
def key48to56(key):
    tmp = [2 for i in range(56)]
    for i in range(len(Data.PC2)):
        tmp[Data.PC2[i] -1] = key[i]    #   dépassement
    res = ''
    for i in tmp:
        res += str(i)

    Bits8Possibles = []
    for i in range(2 ** 8):
        Bits8Possibles.append(bin(i).replace('0b','').zfill(8))
    
    possibleCases = []
    for i in range(2 ** 8):
        tmp = res
        for j in range(8):
            tmp = tmp.replace('2',Bits8Possibles[i][j], 1)
        possibleCases.append(tmp)
    return possibleCases

# permutation at the last of the function F by P
def permutationP(value):
    res = ''
    for i in range(len(value)):
        res += value[Data.P[i] -1]
    return res

# permutation inverse By P
def permutationPInverse(value):
    tmp = [0 for _ in range(len(value))]
    for i in range(len(Data.P)):
        tmp[Data.P[i] - 1]= value[i]
    res = ''
    for i in tmp:
        res += str(i)
    
    return res

def calcul_Inverse_P(value):
    tmp = [0 for i in range(32)]
    for i in range(len(P)):
        tmp[P[i] - 1] = value[i]

    res = ""
    for i in tmp:
        res += str(i)

    return res

def Find6bitsOfK16Possible():
    res = []
    for i in range(64):
        BinaryValue = bin(i).replace("0b", "").zfill(6)
        res.append()
    return res


# Function returning the output value of the S-box for the input value
def calculateSBOXES(value, tabSbox):
    if len(value) != 6:
        exit("Error calculating the S-boxes: len(input) != 6")

    row = value[0] + value[5]
    column = value[1:5]

    row_index = int(row, 2)
    column_index = int(column, 2)

    return bin(tabSbox[row_index * 16 + column_index]).replace("0b", "").zfill(4)

def shift(tab, n):
    return tab[n:] + tab[:n]




    
    