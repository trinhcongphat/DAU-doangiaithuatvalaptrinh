class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}

        # Đếm số lần xuất hiện
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Sắp xếp theo tần suất giảm dần
        sorted_nums = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # Lấy k phần tử đầu
        result = []
        for i in range(k):
            result.append(sorted_nums[i][0])

        return result
