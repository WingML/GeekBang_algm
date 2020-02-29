class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, -1)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, -1)

        # the following cost O(n) extra space, because slice copies the list
        # # nums[:] = nums[::-1]
        # # nums[:k] = nums[:k][::-1]
        # # nums[k:] = nums[k:][::-1]
        # nums[:] = nums[n - k:] + nums[:n - k]

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        """
        Reverse the list with the range nums[left:right] inplace
        """
        if right == -1:
            right = len(nums)

        if left + 1 >= right:
            return
        
        # swap element by element
        mid = (left + right) // 2
        for i in range(mid - left):
            l, r = left + i, right - 1 - i
            nums[l] += nums[r]
            nums[r] = nums[l] - nums[r]
            nums[l] = nums[l] - nums[r]
