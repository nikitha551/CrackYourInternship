class Solution:

    def sameChar(self, A, B):
        # code here
        c=0
        for i in range(len(A)):
            if A[i].lower()==B[i].lower():
                c+=1
        return c
