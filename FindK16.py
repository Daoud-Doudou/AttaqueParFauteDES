import Data
import Utils

def FindKey16(RightEncrypted, FalseEncrypted):
    # wright the rightEncrypted by the format binaire
    BinaryRightEncrypted = Utils.hexToBinary(RightEncrypted);

    BinaryFalseEncrypted = []
    for i in range(len(FalseEncrypted)):
        BinaryFalseEncrypted.append(Utils.hexToBinary(FalseEncrypted[i]))
    
    # find L16 and R16 for the rightEncrypted
    IPRightEncrypted = Utils.permutationIP(BinaryRightEncrypted)
    L16 = IPRightEncrypted[:32].zfill(32)
    R16 = IPRightEncrypted[32:].zfill(32)

    #find L16 and R16 for each FalseEncrypted
    IPFalseEncrypted = []
    L16_false = []
    R16_false = []

    for i in range(len(FalseEncrypted)):
        IPFalseEncrypted.append(Utils.permutationIP(BinaryFalseEncrypted[i]))
        
    for i in (IPFalseEncrypted):
        L16_false.append(i[:32].zfill(32))
        R16_false.append(i[32:].zfill(32))


    #calculate the xor between L16 et each element from L16_false
    XOR_L16_L16False = []
    for i in range(len(L16_false)):
        XOR_L16_L16False.append(Utils.xor(L16, L16_false[i]))

    # calculate the xor betwenn R15 = R16 et each element of R16_false
    XOR_R16_R16False = []                          
    for i in R16_false:
        XOR_R16_R16False.append(Utils.xor(R16, i))

    #calcultate E(R15) = E(R16)
    E_R15 = Utils.expension(R16)

    #calculate E(R15_false)
    E_R15_false = []
    for i in R16_false:
        E_R15_false.append(Utils.expension(i))
        

    # calculate xor between SboxOut and each element of SboxOutfalse    P-1(L16 ^ l16false)   
    XOR_SboxOut_SboxOutFalse = []
    for i in XOR_L16_L16False:              
        XOR_SboxOut_SboxOutFalse.append(Utils.permutationPInverse(i))


    # Initialize a list to hold the potential 6-bit segments of K16
    possible_K16_segments = [[] for _ in range(8)]
    K16 = ''

    # Iterate over each S-box (1 through 8)
    for sbox_index in range(8):
        lastpossible_K16_segments = []
        # Extract the relevant bits for the current S-box
        for xor_val, e_r15_false in zip(XOR_SboxOut_SboxOutFalse, E_R15_false):
            # Get the 4-bit output portion for the current S-box
            sbox_output = xor_val[sbox_index * 4:(sbox_index + 1) * 4].zfill(4)
            
            # Get the 6-bit input portions from the expansion permutations
            e_r15_segment = E_R15[sbox_index * 6:(sbox_index + 1) * 6].zfill(6)
            e_r15_false_segment = e_r15_false[sbox_index * 6:(sbox_index + 1) * 6].zfill(6)
            
            # Try all possible values for the 6-bit segment of K16
            for k_segment in range(64):
                k_segment_bits = bin(k_segment)[2:].zfill(6)
                sbox_input = Utils.xor(e_r15_segment, k_segment_bits)
                sbox_input_false = Utils.xor(e_r15_false_segment, k_segment_bits)
                
                # Calculate S-box outputs and verify if they match the expected S-box output
                if (sbox_output) == Utils.xor(Utils.calculateSBOXES(sbox_input, Data.SBOXES[sbox_index]), Utils.calculateSBOXES(sbox_input_false, Data.SBOXES[sbox_index])):
                    if(len(lastpossible_K16_segments) == 0):
                        possible_K16_segments[sbox_index].append(k_segment_bits)
                    else:
                        if(k_segment_bits in lastpossible_K16_segments):
                            possible_K16_segments[sbox_index].append(k_segment_bits)

            lastpossible_K16_segments = possible_K16_segments[sbox_index]
            possible_K16_segments[sbox_index] = []
        
        
        K16 += lastpossible_K16_segments[0]
    return K16
    

    
    
    
    

    

    



