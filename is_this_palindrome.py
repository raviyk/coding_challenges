class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        p1 = 0
        p2 = n-1
        while(p1 < p2):
            #print(A[p1], A[p2])
            if A[p1] != A[p2]:
                #print('here...')
                return 0
            p1 += 1
            p2 -= 1
        return 1
