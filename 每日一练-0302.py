class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ### Brutal method
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     temp = nums[i+1:]
        #     if diff in temp:
        #         return [i, temp.index(diff) + i + 1]

        # ### hash table - 1
        # hashmap = {}
        # for i, num in enumerate(nums):
        #     hashmap[num] = i

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if hashmap.get(diff) and hashmap[diff] != i:
        #         return [i, hashmap[diff]]

        ### hash table - 2
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[num] = i

        raise Exception("No solution found!")
