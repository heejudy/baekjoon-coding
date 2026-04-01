class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = []

        left = 0
        right = len(height) - 1

        while (left < right):
            amount = (right - left) * (min(height[left], height[right]))
            result.append(amount)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max(result)
        