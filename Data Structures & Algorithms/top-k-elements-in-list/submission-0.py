from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        topK =  counter.most_common(k)

        return [key for key, value in topK]