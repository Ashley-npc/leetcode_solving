liste = [1,5,2,7,3,10,4,5,9,8,11,6]
class Solution(object):
    def twoSum(self, nums, target):
        if(len(nums) >=2 and len(nums) <= 10**4 and target >= -10**9 and target <= 10**9):
            for index,i in enumerate(nums):
                    to_find = target - i

                    if (to_find in nums and i + to_find == target and index != nums.index(to_find)):
                        return [index, nums.index(to_find)]
        else:
            print("verify the length of the list")
