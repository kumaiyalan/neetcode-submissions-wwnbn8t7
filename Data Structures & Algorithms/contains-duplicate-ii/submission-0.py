class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        
        window = set()
        window.add(nums[0])
        L = 0

        for R in range(1, len(nums)):
            while abs(R - L) > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            window.add(nums[R])
        
        return False