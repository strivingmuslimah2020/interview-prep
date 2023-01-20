class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_value = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2 ,-1 ,-1):
            if arr[i] > max_value:
                arr[i], max_value = max_value,arr[i]
            else:
                arr[i] = max_value
        return arr