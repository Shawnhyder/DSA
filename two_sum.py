class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        ind = []

        for i in range(len(nums)):
            t = target - nums[i]
            if(t in myDict):
                ind.append(myDict[t])
                ind.append(i)
                return ind
            else:
                myDict[nums[i]] = i