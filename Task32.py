class Solution:
    def canJump(self, nums: List[int]) -> bool:

        present_ind = 0
        last_ind = len(nums) - 1

        while present_ind < last_ind:
            value = nums[present_ind]
            if not value:
                return False
            if present_ind + value >= last_ind:
                return True
            max = 0
            for i in range(present_ind + 1, present_ind + value + 1):
                if i + nums[i] > max:
                    max = i + nums[i]
                    present_ind = i

        return True