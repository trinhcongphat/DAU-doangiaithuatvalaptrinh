import collections
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # Convert to lowercase and extract words only
        words = re.findall(r'\w+', paragraph.lower())
        
        banned_set = set(banned)
        count = collections.Counter()
        
        for word in words:
            if word not in banned_set:
                count[word] += 1
        
        return count.most_common(1)[0][0]
