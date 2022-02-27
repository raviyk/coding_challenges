class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        import math
        sqrt_a = math.sqrt(A)
        for i in range(1, int(sqrt_a)+1):
            if i**2 == A:
                return i
                exit
        return -1
