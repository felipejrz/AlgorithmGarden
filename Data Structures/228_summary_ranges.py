# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         listf = []
#         first = None
#         last = None
#         prev = None
#         for i in range(len(nums)):
#             if i == 0:
#                 first = nums[i]
#                 prev = nums[i]

#             if nums[i] - prev == 1:
#                 last = nums[i]
#             else:
#                 if last != None:
#                     if first == last:
#                         listf += [f'{first}']
#                     else:
#                         listf += [f'{first}->{last}']
#                 first = nums[i]
#                 last = nums[i]
#             prev = nums[i]


#             if i == len(nums) - 1:
#                 if first == last:
#                     listf += [f'{first}']
#                 else:
#                     listf += [f'{first}->{last}']
#         return listf
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        first = nums[0]
        listf = []

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                if first == nums[i - 1]:
                    listf += [f"{first}"]
                else:
                    listf += [f"{first}->{nums[i - 1]}"]
                first = nums[i]

        if first == nums[-1]:
            listf += [f"{first}"]
        else:
            listf += [f"{first}->{nums[-1]}"]
        return listf
