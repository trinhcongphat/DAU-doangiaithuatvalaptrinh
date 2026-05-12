class Solution:
    def canAliceWin(self, nums):
        single = 0
        double = 0

        for x in nums:
            if x < 10:
                single += x
            else:
                double += x

        return single != double