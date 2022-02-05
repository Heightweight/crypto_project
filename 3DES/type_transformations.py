def bytes_to_list(P):
    l = len(P) * 8
    result = [0] * l
    pos = 0
    for ch in P:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                result[pos] = 1
            else:
                result[pos] = 0
            pos += 1
            i -= 1
    return result

def list_to_bytes(C):
    result = []
    pos = 0
    c = 0
    while pos < len(C):
        c += C[pos] << (7 - (pos % 8))
        if (pos % 8) == 7:
            result.append(c)
            c = 0
        pos += 1
    return bytes(result)

def list_xor(list1, list2):
    if len(list1) != len(list2):
        raise "Różne długości list dla operacji XOR!"
    result = []
    for (i,j) in zip(list1,list2):
        result += [i ^ j]
    return result
