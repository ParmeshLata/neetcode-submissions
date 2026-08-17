class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                output.append(i+1)
                output.append(j+1)
                break
            if numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1
        return output