class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_dict={}
        for num in nums:
            if num in temp_dict:
                temp_dict[num]+=1
            else:
                temp_dict[num]=1
        
        output=[]
        num=0
        freq=0
        for i in range(k):
            for key,value in temp_dict.items():
                if value>freq:
                    freq=value
                    num=key
            output.append(num)
            temp_dict[num]=0
            num=0
            freq=0
        
        return output