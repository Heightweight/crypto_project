from type_transformations import *


def PC_1(K):
    PC1_indexes = [57, 49, 41, 33, 25, 17, 9,
                  1, 58, 50, 42, 34, 26, 18,
                  10, 2, 59, 51, 43, 35, 27,
                  19, 11, 3, 60, 52, 44, 36,
                  63, 55, 47, 39, 31, 23, 15,
                  7, 62, 54, 46, 38, 30, 22,
                  14, 6, 61, 53, 45, 37, 29,
                  21, 13, 5, 28, 20, 12, 4]
    return list(map(lambda x: K[x - 1], PC1_indexes))


def left_shift(i, B):
    #tam gdzie przesuniecie o 1
    if i == 0 or i == 1 or i == 8 or i == 15:
        B = B[1:] + [B[0]]
    #tam gdzie przesuniecie o 2
    else:
        B = B[2:] + [B[0]] + [B[1]]
    return B


def PC_2(K):
    PC2_indexes = [14, 17, 11, 24, 1, 5,
                  3, 28, 15, 6, 21, 10,
                  23, 19, 12, 4, 26, 8,
                  16, 7, 27, 20, 13, 2,
                  41, 52, 31, 37, 47, 55,
                  30, 40, 51, 45, 33, 48,
                  44, 49, 39, 56, 34, 53,
                  46, 42, 50, 36, 29, 32]
    return list(map(lambda x: K[x - 1], PC2_indexes))


def key_schedule(K):
    K_i = [0] * 16

    # wybór znaczących bitów za pomocą PC-1
    PC1 = PC_1(K)

    # podział na C1 i D1
    C_i = PC1[:28]
    D_i = PC1[28:]

    # 16 powtórzeń left_shift->PC-2
    for i in range(16):
        C_i = left_shift(i, C_i)
        D_i = left_shift(i, D_i)
        K_i[i] = PC_2(C_i + D_i)

    return K_i


def IP(I):
    IP_indexes = [58, 50, 42, 34, 26, 18, 10, 2,
                  60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6,
                  64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17, 9, 1,
                  59, 51, 43, 35, 27, 19, 11, 3,
                  61, 53, 45, 37, 29, 21, 13, 5,
                  63, 55, 47, 39, 31, 23, 15, 7]
    return list(map(lambda x: I[x - 1], IP_indexes))


def IP_1(I):
    IP_indexes = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]
    return list(map(lambda x: I[x - 1], IP_indexes))


def E(R):
    E_indexes = [32, 1, 2, 3, 4, 5,
                 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]
    return list(map(lambda x: R[x - 1], E_indexes))


def S(i, B):
    if i == 0:
        S = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
             0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
             4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
             15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    elif i == 1:
        S = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
             3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
             0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
             13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    elif i == 2:
        S = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
             13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
             13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
             1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    elif i == 3:
        S = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
             13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
             10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
             3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    elif i == 4:
        S = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
             14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
             4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
             11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    elif i == 5:
        S = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
             10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
             9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
             4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    elif i == 6:
        S = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
             13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
             1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
             6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    elif i == 7:
        S = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
             1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
             7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
             2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    SB=[0]*4

    # znalezienie wspolrzednych szukanej wartosci
    i = (B[0] << 1) + B[5]
    j = (B[1] << 3) + (B[2] << 2) + (B[3] << 1) + B[4]

    # wskazanie wartosci na podstawie współrzędnych
    v = S[(i << 4) + j]

    # rozpisanie na bity
    SB[0] = (v & 8) >> 3
    SB[1] = (v & 4) >> 2
    SB[2] = (v & 2) >> 1
    SB[3] = v & 1

    return SB


def P(L):
    P_indexes = [16, 7, 20, 21,
                 29, 12, 28, 17,
                 1, 15, 23, 26,
                 5, 18, 31, 10,
                 2, 8, 24, 14,
                 32, 27, 3, 9,
                 19, 13, 30, 6,
                 22, 11, 4, 25]
    return list(map(lambda x: L[x - 1], P_indexes))


def f(R, K):
    # XOR klucza i bloku R przekształconego za pomocą E
    B = list_xor(K, E(R))
    SB = []

    # podział na 8 części i przepuszczenie ich przez S-boxy
    for i in range(8):
        SB += S(i, B[i * 6:(i + 1) * 6])
    return P(SB)


def des_encrypt(I, K):
    #weryfikacja poprawnosci danych
    if len(I) != 64:
        print("Dlugość bloku do zaszyforwania: " + str(len(I)))
        raise "Blok do zaszyfrowania złej długości!"
    if len(K) != 64:
        print("Dlugość klucza: " + str(len(K)))
        raise "Klucz złej długości!"
# --szyfrowanie des
    # key_schedule
    K_i = key_schedule(K)

    # poczatkowa permutacja
    P = IP(I)

    # pierwsze 15 rund szyfrowania
    for i in range(15):
        L_i = P[:32]
        R_i = P[32:]

        L_ip1 = R_i
        R_ip1 = list_xor(L_i, f(R_i, K_i[i]))
        P = L_ip1 + R_ip1

    # ostatnia runda szyfrowania
    L_i = P[:32]
    R_i = P[32:]

    L_ip1 = R_i
    R_ip1 = list_xor(L_i, f(R_i, K_i[15]))
    P = R_ip1 + L_ip1

    # końcowa permutacja
    C = IP_1(P)
# --koniec szyfrowania des
    return C


def des_decrypt(C, K):
    # weryfikacja poprawnosci danych
    if len(C) != 64:
        print("Dlugość bloku do zaszyforwania: " + str(len(C)))
        raise "Blok do zaszyfrowania złej długości!"
    if len(K) != 64:
        print("Dlugość klucza: " + str(len(K)))
        raise "Klucz złej długości!"
# --deszyfrowanie des
    # key_schedule
    K_i = key_schedule(K)

    # poczatkowa permutacja
    P = IP(C)

    # pierwsze 15 rund szyfrowania
    for i in range(15):
        L_i = P[:32]
        R_i = P[32:]

        L_ip1 = R_i
        R_ip1 = list_xor(L_i, f(R_i, K_i[15-i]))
        P = L_ip1 + R_ip1

    # ostatnia runda szyfrowania
    L_i = P[:32]
    R_i = P[32:]

    L_ip1 = R_i
    R_ip1 = list_xor(L_i, f(R_i, K_i[0]))
    P = R_ip1 + L_ip1

    # końcowa permutacja
    I = IP_1(P)
# ---------------koniec deszyfrowania des
    return I

def tdea_encrypt(I, K_1, K_2):
    # 3DES zgodny z trybem K1 = K3
    return des_encrypt(des_decrypt(des_encrypt(I, K_1), K_2), K_1)


def tcfb_encrypt(P, K, IV, KEY):
    # weryfikacja poprawnosci danych
    if isinstance(P, str):
        try:
            P = P.encode('ascii')
        except UnicodeEncodeError:
            raise "Niepoprawnie kodowanie danych do zaszyfrowania!"
    if isinstance(P, bytes):
        data = bytes_to_list(P)
        print("Szyfrowana jest wiadomość: \n" + str(data) + ".")
        if isinstance(K, int) and K <= 64:
            if isinstance(IV, bytes):
                if isinstance(KEY,str):
                    try:
                        KEY = KEY.encode('ascii')
                    except UnicodeEncodeError:
                        raise "Niepoprawnie kodowanie klucza!"
                if isinstance(KEY, bytes):
                    key = bytes_to_list(KEY)
# ------------------szyfrowanie tcfb

                    # wyodrebnienie kluczy
                    Key_1 = key[:64]
                    Key_2 = key[64:]

                    # przypisanie wartosci IV do Input'u
                    I_i = bytes_to_list(IV)
                    if len(I_i) > 64:
                        raise "Zbyt długie IV!"
                    elif len(I_i) < 64:
                        I_i = [0] * (64 - len(I_i)) + I_i
                    print("Wykorzystywane IV: \n" + str(I_i))

                    # zastosowanie ewentualnego paddingu
                    if len(data) % K != 0:
                        padding_length = K - (len(data) % K)
                        print("Dodawany jest padding wielkości: " + str(padding_length))
                        data = data + [0] * padding_length
                        print("Szyfrowana jest wiadomość z paddingiem: \n" + str(data) + ".")

                    C = []

                    # kolejne segmenty szyfrowania bloków w trybie CFB
                    for i in range(int(len(data) / K)):
                        print("Szyfrowanie od " + str(i * K) + " do " + str((i + 1) * K) + " bitów bloku danych.")
                        P_i = data[i * K:(i + 1) * K]
                        O = tdea_encrypt(I_i,Key_1, Key_2)
                        C_i = list_xor(P_i, O[:K])
                        C += C_i
                        I_i = I_i[K:] + C_i
                    print("Zaszyfrowana wiadomość w bitach: \n" + str(C))
                    cyphertext = list_to_bytes(C).hex()
                    print("Zaszyfrowana wiadomość: " + str(cyphertext))
                    return cyphertext
# ------------------koniec szyfrowania tcfb
                else:
                    raise "Niepoprawny typ klcza!"
            else:
                raise "Niepoprawny typ parametru IV!"
        else:
            raise "Niepoprawna wartość parametru K!"
    else:
        raise "Niepoprawny typ wiadomości do zakodowania!"


def tcfb_decrypt(C, K, IV, KEY):
    # weryfikacja poprawnosci danych
    if isinstance(C, str):
        try:
            C = C.encode('ascii')
        except UnicodeEncodeError:
            raise "Niepoprawnie kodowanie danych do odszyfrowania!"
    if isinstance(C, bytes):
        data = bytes_to_list(C)
        print("Deszyfrowana jest wiadomość: \n" + str(data) + ".")
        if isinstance(K, int) and K <= 64:
            if isinstance(IV, bytes):
                if isinstance(KEY,str):
                    try:
                        KEY = KEY.encode('ascii')
                    except UnicodeEncodeError:
                        raise "Niepoprawnie kodowanie klucza!"
                if isinstance(KEY, bytes):
                    key = bytes_to_list(KEY)
# ------------------deszyfrowanie tcfb

                    # wyodrebnienie kluczy
                    K_1 = key[:64]
                    K_2 = key[64:]

                    # przypisanie wartosci IV do Input'u
                    I_i = bytes_to_list(IV)
                    if len(I_i) > 64:
                        raise "Zbyt długie IV!"
                    elif len(I_i) < 64:
                        I_i = [0] * (64 - len(I_i)) + I_i
                    print("Wykorzystywane IV: \n" + str(I_i))

                    # zastosowanie ewentualnego paddingu
                    if len(data) % K != 0:
                        padding_length = K - (len(data) % K)
                        print("Dodawany jest padding wielkości: " + str(padding_length))
                        data = data + [0] * padding_length
                        print("Deszyfrowana jest wiadomość z paddingiem: \n" + str(data) + ".")

                    P = []

                    # kolejne segmenty deszyfrowania bloków w trybie CFB
                    for i in range(int(len(data) / K)):
                        print("Deszyfrowanie od " + str(i * K) + " do " + str((i + 1) * K) + " bitów bloku danych.")
                        C_i = data[i * K:(i + 1) * K]
                        O = tdea_encrypt(I_i,K_1, K_2)
                        P_i = list_xor(C_i, O[:K])
                        P += P_i
                        I_i = I_i[K:] + C_i
                    print("Odszyfrowana wiadomość w bitach: \n" + str(P))
                    plaintext = list_to_bytes(P).hex()
                    print("Odszyfrowana wiadomość: " + str(plaintext))
                    return plaintext
# ------------------koniec deszyfrowania tcfb
                else:
                    raise "Niepoprawny typ klcza!"
            else:
                raise "Niepoprawny typ parametru IV!"
        else:
            raise "Niepoprawna wartość parametru K!"
    else:
        raise "Niepoprawny typ wiadomości do zakodowania!"
