class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = [[int(0)] * n for _ in range(m)]
        for i in range(m):
            nums=original[i*n: (i+1)*n]
            for j in range(n):
                ans[i][j]=nums[j]
        return(ans)
                    
                    