class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = dict()
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result