def MaxSubArray(nums,k)
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
