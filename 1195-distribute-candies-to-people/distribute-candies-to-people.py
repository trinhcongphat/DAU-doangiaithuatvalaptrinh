class Solution:
    def distributeCandies(self, candies, num_people):
        result = [0] * num_people
        give = 1
        i = 0
        
        while candies > 0:
            result[i] += min(give, candies)
            candies -= give
            give += 1
            i = (i + 1) % num_people
        
        return result
