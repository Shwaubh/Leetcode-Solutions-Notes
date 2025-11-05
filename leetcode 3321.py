from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], K: int, X: int) -> List[int]:
        top_x = SortedList()
        bottom = SortedList()
        counter = Counter()
        curr_sum = 0

        def update(curr, qty):
            nonlocal curr_sum
            if counter[curr]:
                try:
                    bottom.remove( (counter[curr], curr) )
                except:
                    top_x.remove( (counter[curr], curr) )
                    curr_sum = curr_sum - counter[curr]*curr
            counter[curr] += qty
            if counter[curr]:
                bottom.add( (counter[curr], curr) )
        
        res = []
        for i in range(len(nums)):
            update(nums[i], 1)
            if i >= K:
                update(nums[i-K], -1)
            
            while bottom and len(top_x) < X:
                freq, element = bottom.pop()
                top_x.add( (freq, element) )
                curr_sum = curr_sum + freq*element
            
            while bottom and bottom[-1] > top_x[0]:
                fb, eb = bottom.pop()
                ft, et = top_x.pop(0)
                curr_sum = curr_sum - ft*et
                bottom.add((ft, et))
                top_x.add((fb, eb)) 
                curr_sum = curr_sum + fb*eb

            if i >= K-1:
                res.append(curr_sum)
        
        return res

