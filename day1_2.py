class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,n in enumerate(nums):
            d=target-n
            if d in map:
                return [map[d],i]
            map[n]=i
