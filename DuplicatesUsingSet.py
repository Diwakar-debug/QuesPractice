class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        d = set()
        for each in A:
            if each in d:
                return each
            else:
                d.add(each)
        return -1