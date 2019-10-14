class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        length = len(nums)
        temp1 = nums[:(length-1)//2+1][::-1]
        print(temp1)
        temp2 = nums[(length-1)//2+1:][::-1]
        ti=0
        for i in range(0, length, 2):
            nums[i]=temp1[ti]
            ti+=1
        ti=0
        for i in range(1, length, 2):
            nums[i]=temp2[ti]
            ti+=1