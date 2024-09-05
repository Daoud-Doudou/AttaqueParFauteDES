from FindK16 import FindKey16
from FindK import find_key_from_k16


# Mon message clair :
message = "DC 2C 54 08 2A B5 54 07"

#  Mon message chiffre juste :
RightEncrypted = "32 AA 80 8A 49 F5 54 29"

#  Mes messages chiffres faux :
FalseEncrypted = ["7A AA 94 8A 11 A5 54 28", 
                "72 AB 80 0A 49 B5 11 74", 
                "26 AA 88 8B 09 E5 74 29", 
                "32 2B 80 9A 48 75 10 3D", 
                "3B BA 84 CE 4B E0 54 29", 
                "66 AA C0 92 09 B1 50 08", 
                "33 AA A0 8A 5D F5 46 29", 
                "36 2A C0 9A 48 D5 10 29", 
                "31 EB 80 CA 5B F4 54 2D", 
                "22 EA C4 AB 09 E5 45 2B", 
                "72 BA 82 8A 49 F4 5C 28", 
                "36 8A C0 8A 4D D5 55 29", 
                "30 AE 80 8E C8 F4 50 3D", 
                "73 FA 84 C8 59 B4 55 60", 
                "32 AF 88 8B 09 E5 D4 29", 
                "32 8A 80 8A 4D BD 55 28", 
                "A6 AF 81 9A C9 F5 50 39", 
                "72 BE 80 82 09 B0 54 B8", 
                "33 AA 00 9A 59 F5 16 29", 
                "32 A2 80 8A 09 A9 54 28", 
                "B6 AA C0 8A 68 F5 05 69", 
                "32 EB 84 0B 09 E5 10 3F", 
                "26 BA 82 8A 49 F4 74 29", 
                "33 E2 84 8A 19 E3 54 29", 
                "02 AA D0 8A 6D B5 45 29", 
                "27 FA C4 D8 59 F4 50 09", 
                "32 AF A0 8A 4D F5 C4 29", 
                "33 E8 84 CA 59 F6 54 29", 
                "12 AA 90 8B 01 F5 44 68", 
                "22 BE C0 AA 49 F4 45 B9", 
                "72 AA 00 9A 49 F5 1C 28", 
                "32 A9 80 CA 49 74 54 3D"]


if __name__ == '__main__':
    K16 = FindKey16(RightEncrypted, FalseEncrypted)
    K = find_key_from_k16(K16, message, RightEncrypted)

    print("La cle K16 est : " + K16)
    print("La cle K est : " + K)
