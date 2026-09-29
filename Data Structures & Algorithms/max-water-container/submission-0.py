class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights)-1
        area = 0

        while left <= right:
            width = right - left
            minNum = min(heights[left],heights[right])
            areaCalc = minNum*width
            area = max(area,areaCalc)

            if heights[left] < heights[right]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                right-=1

        return area

        