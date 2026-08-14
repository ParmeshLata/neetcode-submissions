class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        condition_product=1
        cnt_0=0
        ind_0=-1
        for i in range(len(nums)):
            if nums[i]==0:
                product=product*nums[i]
                cnt_0+=1
                ind_0=i
            else:
                condition_product=condition_product*nums[i]
                product=product*nums[i]
        if cnt_0>=2:
            return [0]*len(nums)
        if cnt_0==0:
            output=[]
            for num in nums:
                output.append(product//num)
            return output
        if cnt_0==1:
            output=[0]*len(nums)
            output[ind_0]=condition_product
            return output