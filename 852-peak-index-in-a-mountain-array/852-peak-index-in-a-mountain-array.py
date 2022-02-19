class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        mid = (left + right)//2
        while left < right:
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
            mid = (left + right)//2    
        return mid
        