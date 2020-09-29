class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        i = 0
        j = n-1
        run = 0
        while(i<=j):
            if A[i]%2!=0 and A[j]%2==0:
                swap = A[i]
                A[i] = A[j]
                A[j] = swap
                i = i + 1
                j = j -1
            elif A[i]%2==0 and A[j]%2!=0:
                i = i+1
                j = j-1
            elif A[i]%2!=0 and A[j]%2!=0:
                j = j -1
            elif A[i]%2==0 and A[j]%2==0:
                i = i +1

        return A
        
