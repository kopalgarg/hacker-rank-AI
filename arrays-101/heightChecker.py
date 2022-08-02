class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        rp = 0
        for i in range(len(heights)):
            if heights[rp] > min(heights[rp:]):
                ind = heights[rp:].index(min(heights[rp:]))
                hold = heights[rp]
                heights[rp] = min(heights[rp:])
                heights[rp+ind] = hold
                rp += 1
            else:
                rp += 1
        return heights
            
        