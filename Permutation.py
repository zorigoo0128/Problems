import math
class Solution:

    def getPermutation(self, n: int, k: int) -> str:

        arr = [ str(x) for x in range(1, n + 1) ]
        total = 1
        for i in range(2,n):
            total *= i
        k -= 1

        result = []

        for i in range( n-1, -1, -1 ):

            ind = k//total

            result += [arr.pop(ind)]

            k -= total * ind
            total = total//i if i > 0 else total
            

        return ''.join(result)
    

# Driver's code
if __name__ == "__main__":

    s = Solution()

    result = s.getPermutation(4, 7)



    print(result)

 