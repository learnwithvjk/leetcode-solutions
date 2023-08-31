class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        swapIndex = 0
        if len(nums) == 0:
            return result

        for index, item in enumerate(nums):
            if item != val:
                temp = nums[swapIndex]
                nums[swapIndex] = nums[index]
                nums[index] = temp
                swapIndex += 1
        return swapIndex


def getExecutable(*args):
    return Solution().removeElement(*args)
