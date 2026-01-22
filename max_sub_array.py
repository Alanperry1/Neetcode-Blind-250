def MaxSubArray(nums,k):
    # Time Complexity: O(n) - O(k) initial sum + O(n-k) sliding window = O(n)
    # Space Complexity: O(1) - only using constant extra space
    l,r=0,k-1
    initialSum=sum(nums[l:r+1])
    maxSum=initialSum
    while r<len(nums)-1:
        win_sum=initialSum+nums[r+1]-nums[l]
        l+=1
        r+=1
        initialSum=win_sum
        maxSum=max(win_sum,maxSum)
    return maxSum
