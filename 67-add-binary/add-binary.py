class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = ""

        while i >= 0 or j >= 0 or carry:
            s = carry

            if i >= 0:
                s += int(a[i])
                i -= 1

            if j >= 0:
                s += int(b[j])
                j -= 1

            ans += str(s % 2)
            carry = s // 2

        return ans[::-1]