class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range((m + n) - 1, -1, -1):
            # Condicion de and nums2 que verifique que esta lista no este vacia
            if nums1[i] == 0 and nums2:
                nums1[i] = nums2[-1]
                del nums2[-1]
        nums1.sort()
