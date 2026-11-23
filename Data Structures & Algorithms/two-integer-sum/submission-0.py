class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       complement = 0  
       bag = dict()
       for k, v in enumerate(nums):
            complement = target-v
            if complement in bag.keys():
                return [bag.get(complement), k]
            else:
                bag[v] = k
            complement = 0

