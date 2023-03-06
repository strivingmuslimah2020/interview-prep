class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:    
        stack = []
        total = 0
        n = len(arr)
        for i in range(n+1):
            
            while  stack and( i ==  n or arr[stack[-1]] >= arr[i]):
                val = stack.pop()

                if len(stack) == 0:
                    prev_val = -1
                    
                else:    
                    prev_val = stack[-1]    
                next_val = i

                
                
                
                contr = arr[val] * (next_val - val) * (val - prev_val)
                total += contr
                
                
                
                
            stack.append(i)
        
        MOD = (10**9)+7
        return total  % MOD