class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        ans = float('inf')
        for t2 in range(n):
            h2 = A[t2]
            c2 = B[t2]
            c1 = float('inf')
            for t1 in range(t2):
                if A[t1] < h2:
                    c1 = min(c1, B[t1])                
            c3 = float('inf')
            for t3 in range(t2+1, n):
                if A[t3] > h2:
                    c3 = min(c3, B[t3])
            c = c1 + c2 + c3
            #print(c1, c2, c3)
            ans = min(c, ans)
        if ans == float('inf'):
            return -1
        else:
            return ans                
