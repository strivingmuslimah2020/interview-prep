class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr = sorted(arr)
        arr[0] = 1
        for i in range(1,len(arr)):
            
            if abs(arr[i] - arr[i - 1]) <= 1:
                continue
            else:
                arr[i] = arr[i - 1]  + 1
                    
        return max(arr)