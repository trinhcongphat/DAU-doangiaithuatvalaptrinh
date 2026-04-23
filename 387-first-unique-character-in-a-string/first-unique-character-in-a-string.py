class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        
        # Đếm số lần xuất hiện
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Tìm ký tự xuất hiện 1 lần đầu tiên
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1
