# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。 
# 
#  说明: 
# 
#  
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n。 
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
#  
# 
#  示例: 
# 
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
#  Related Topics 数组 双指针

# 1、暴力插入，时间复杂度 O(min(m, n)^2)
# 2、双指针，从前往后，空间复杂度至少 O(m)
# 3、双指针，从后往前，空间复杂度 O(1)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # idx = m + n - 1
        # idx1, idx2 = m - 1, n - 1
        #
        # while idx1 >=0 and idx2 >= 0:
        #     if nums1[idx1] <= nums2[idx2]:
        #         nums1[idx] = nums2[idx2]
        #         idx2 -= 1
        #     else:
        #         nums1[idx] = nums1[idx1]
        #         idx1 -= 1
        #     idx -= 1
        #
        # # nums1[:idx2+1] = nums2[:idx2+1]
        # for i in range(idx2 + 1):
        #     nums1[i] = nums2[i]

        # shorter solution
        while n:
            if m and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

# leetcode submit region end(Prohibit modification and deletion)
