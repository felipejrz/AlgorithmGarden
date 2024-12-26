class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for count, i in enumerate(nums):
            if i in dic:
                if abs(dic[i] - count) <= k:
                    return True
            dic[i] = count
        return False
