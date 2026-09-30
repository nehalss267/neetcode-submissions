class Solution:
    def reverseBits(self, n: int) -> int:
        binaryStr = ""
        for i in range(32):
            if n & (1 << i):
                binaryStr += "1"
            else:
                binaryStr += "0"

        res = 0
        for i, bit in enumerate(binaryStr[::-1]):
            if bit == "1":
                res |= (1 << i)

        return res