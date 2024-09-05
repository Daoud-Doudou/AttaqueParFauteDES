from Utils import key64to56, shift, key56to48, expension, xor, calculateSBOXES, permutationP, permutationIP, permutationIPInverse, hexToBinary
from Data import NbrRotation, SBOXES

#  Fonction permettant de generer les 16 sous-cles a partir de K
def key_scheduler(k):
    PC1_K = key64to56(k)

    L0 = PC1_K[:28]
    R0 = PC1_K[28:]

    Li_Ri = []
    for shiftValue in NbrRotation:
        L0 = shift(L0, shiftValue)
        R0 = shift(R0, shiftValue)
        Li_Ri.append((L0, R0))

    keys = []
    for Li, Ri in Li_Ri:
        tmp = Li + Ri
        keys.append(key56to48(tmp))

    return keys


#  Fonction permettant de faire le calcul de F
def fonction_F(ri, key):
    E_ri = expension(ri)

    E_riXorKi = xor(E_ri, key)

    SBoxOut = ""
    for i in range(0, 48, 6):
        SBoxOut += calculateSBOXES(E_riXorKi[i:i + 6], SBOXES[i // 6])

    P_SBoxOut = permutationP(SBoxOut)

    return P_SBoxOut


#  Fonction retournant le message chiffre par le DES
def EncryptDes(hexMsg, hexK):
    msg = hexToBinary(hexMsg)
    k = hexToBinary(hexK)

    keys = key_scheduler(k)

    IP_msg = permutationIP(msg)

    L0 = IP_msg[:32]
    R0 = IP_msg[32:]

    Li_old = L0
    Ri_old = R0
    for i in range(16):
        Li = Ri_old
        Ri = xor(Li_old, fonction_F(Ri_old, keys[i]))

        Li_old = Li
        Ri_old = Ri

    cipher = permutationIPInverse(Ri + Li)

    return hex(int(cipher, 2)).replace('0x', '').zfill(16)