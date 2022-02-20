class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
#        print(A)
#        print(B)
#        print(len(B))

        #Get prefix sum
        ps = [0]*len(A)
        ps[0] = A[0]
        for i in range(1, len(A)):
            ps[i] = ps[i-1] + A[i]

        sum_list = []
        for i in range(0, len(B)):
            s = B[i][0] - 1
            e = B[i][1] - 1
            # for j in range(s, e+1):
            #     sum = sum + A[j]
            # sum_list.append(sum)
            sum_temp = 0
            if s == 0:
                sum_temp = ps[e]
            else:
                sum_temp = ps[e] - ps[s-1]
            #print('s: ', s, 'e: ', e)
            sum_list.append(sum_temp)
#        print('s: ', s, 'e: ', e)
        return sum_list
        
