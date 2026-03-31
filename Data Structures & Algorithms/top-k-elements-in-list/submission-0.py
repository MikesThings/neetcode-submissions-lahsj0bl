class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
        
        # Step 2: Sort the frequency map by value in descending order
        sorted_items = sorted(numMap.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Extract the top k frequent elements
        ret = []
        for i in range(k):
            ret.append(sorted_items[i][0])
        
        return ret
