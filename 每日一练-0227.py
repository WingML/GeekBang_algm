class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return l
        new_idx = 0
        for i in range(1, l):
            if nums[new_idx] == nums[i]:
                continue
            if i > new_idx + 1:
                nums[new_idx + 1] = nums[i]
            new_idx += 1
            

        # for num in nums[1:]:
        #     if nums[new_idx] == num:
        #         continue
        #     new_idx += 1
        #     nums[new_idx] = num
        return new_idx + 1
