class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits=0 # init to 0
        orig_n=n
        for _ in range(0,32):
            reversed_bits <<= 1 # rotate to left by 1 so now the right most digit =0
            reversed_bits += n % 2 # if n%2=1, add 1, else 0
            n>>=1 # look at the next bit by rotating to right 
        return reversed_bits
        

                
            
        