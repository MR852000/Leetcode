class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # This pointer tracks where to place the next unique element
        write_index = 1 
        
        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current number is different from the previous one, it's unique!
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        # LeetCode expects you to return the count of unique elements
        return write_index