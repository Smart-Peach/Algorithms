class Solution:
    def canJump(self, nums: List[int]) -> bool:

        present_ind = 0
        finish_ind = len(nums) - 1
        able_steps = nums[0]

        while able_steps and present_ind < finish_ind:
            able_steps -= 1
            present_ind += 1

            if nums[present_ind] > able_steps:
                able_steps = nums[present_ind]

        if present_ind == finish_ind:
            return True
        return False
