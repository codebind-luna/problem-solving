def minPowersOfTwo(number):
    comple = (1 << number.bit_length()) - number
    pos = neg = 0
    while number:
        number, bit = divmod(number, 2)
        comple, comple_bit = divmod(comple, 2)
        pos += bit
        neg += comple_bit
        pos, neg = min(pos, 1 + neg), min(neg, 1 + pos)
    return pos


print(minPowersOfTwo(int(input("Please Enter the Number:"))))