
class Solution:
    def __init__(self): # Constructor
        pass
    
    def checkValid(self, a, ind):

        desc = set()
        asc = set()
        n = len(a)
        for i in range(ind):
            desc.add( i - a[i] )
            asc.add( n - 1 - i - a[i]  )

        return len(desc) == len(asc) and len(asc) == ind

    

    def bt(self, d, ind, s, r):

        if not self.checkValid(d, ind):
            return

        if not s:
            r[0] +=1
            return

        for e in s:
            d[ind] = e
            self.bt( d, ind + 1, s.difference({e}), r)



    def SolveNQueens(self, n : int):

        d = [-1] * n
        s = set( [x for x in range(n)] )
        count = [0]
        self.bt( d, 0, s, count )

        return count[0]



# Driver's code
if __name__ == "__main__":

    s = Solution()

    result = s.SolveNQueens(4)

    print(result)

    
