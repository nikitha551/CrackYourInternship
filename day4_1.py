def majorityElement(self, nums: List[int]) -> int:
        r=0
        c=0
        for n in nums:
            if c==0:
                r=n
            c+=(1 if n==r else -1)
        return r
