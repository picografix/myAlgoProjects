#maximum sub-arrays problem 
""" We will define and divide and conquer algorithm on solving maximum sub array problem"""
#  a maximum sub array has only three posibility that it can either lie on left half or on right half or crosses the mid point
# using this property we will define a function to find maximum crossing subarray and also find subarrays in respective halfs and then comapre their sum to find which is maximum we will do all this recursively
def crossingSubarr(A,l,u):
    left_sum = -21000
    temp_sum=0
    mid = (l+u)//2
    left_index = mid
    for i in reversed(range(l,mid)):
        temp_sum += A[i]
        if left_sum < temp_sum :
            left_sum = temp_sum
            left_index = i
    right_sum = -21000
    rtemp_sum=0
    right_index = mid
    for i in range(mid,u):
        rtemp_sum += A[i]
        if rtemp_sum > right_sum:
            right_sum = rtemp_sum
            right_index = i
    return (left_sum+right_sum,left_index,right_index)
#now since we have defined the crosing subarray we can now recursively define our main subarray giving function
def maxSubArr(A):
    l= 0
    u= len(A)
    if u==0:
        return (0,l,u)
    elif u==1:
        return (A[0],l,u)
    else:
        mid = (l+u)//2
        left_sum,left_low,left_high = maxSubArr(A[l:mid])
        right_sum,right_low,right_high = maxSubArr(A[mid:u])
        cross_sum,cross_left,cross_right = crossingSubarr(A[l:u],l,u)
        maxi =  max(left_sum,right_sum,cross_sum)
        if maxi == left_sum:
            return (left_sum,left_low,left_high)
        elif maxi == right_sum:
            return (right_sum,right_low,right_high)
        else :
            return (cross_sum,cross_left,cross_right)
ans = maxSubArr([-6,5,4,3,2,-1])
print(ans[0])