class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        
        size=0
        while i<j:
            size=max(size, (j-i)*min(heights[i], heights[j]))
            if heights[i]==heights[j]:
                i+=1
                j-=1
            else:
                if heights[i]>heights[j]:
                    j-=1
                else:
                    i+=1
        return size