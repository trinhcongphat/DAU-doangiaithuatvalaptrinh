class Solution:
    def sortPeople(self, names, heights):
        people = list(zip(heights, names))   # ghép height với name
        
        people.sort(reverse=True)            # sắp xếp giảm dần theo height
        
        result = []
        for h, name in people:
            result.append(name)
            
        return result
