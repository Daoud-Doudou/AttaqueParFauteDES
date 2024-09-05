from DES import EncryptDes
from Utils import hexToBinary, key56to64, key48to56


#  Fonction permettant de retrouver la cle K a partir de la sous-cle K16
def find_key_from_k16(K16, msgClair, chiffreJuste):
    L16R16 = key48to56(K16)

    keysWithoutSignByte = []
    for L0R0 in L16R16:
        keysWithoutSignByte.append(key56to64(L0R0))

    keys = []
    for j in keysWithoutSignByte:
        key = ""
        for i in range(0, len(j), 8):
            octet = j[i:i + 8]
            count = octet.count("1")
            if count % 2 == 0:
                octet = octet.replace("2", "1")
            else:
                octet = octet.replace("2", "0")
            key += octet
        keys.append(hex(int(key, 2)).replace('0x', '').zfill(16))

    for key in keys:
        c = EncryptDes(msgClair, key)
        if c == chiffreJuste.lower().replace(' ', ''):
            trueKey = key

    return trueKey