class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        # A = list(A)
        def reverse(s, st, en):
            s = list(s)
            p1 = st
            p2 = en
            while(p1 < p2):
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
            return ''.join(s[st:en+1])

        rev_A = list(''.join(reverse(A, 0, n-1)))
        p1 = 0
        p2 = 0
        res = []
        i = 0
        while(p1 < n or p2 < n):
            while(p2 < n and rev_A[p2] !=' '):
                p2 += 1
            i += 1
            res.append(reverse(rev_A, p1, p2-1))
            p1 = p2+1
            p2 = p1
        res = ' '.join(res)            
        return res.lstrip()
