'''
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    Follow up: The overall run time complexity should be O(log (m+n)).

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

    Input: nums1 = [0,0], nums2 = [0,0]
    Output: 0.00000

    Input: nums1 = [], nums2 = [1]
    Output: 1.00000
'''

import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        for _ in range(len(nums2)):
            nums1.append(nums2[_])
        print(nums1)
        nums1.sort()
        leng = len(nums1)
        if leng % 2 ==0:
            print(leng)
            med = (nums1[int(leng/2)] + nums1[int((leng+1)/2)]) / 2
        else:
            leng = len(nums1)
            leng = leng
            med =  nums1[int(leng/2)]
        return math.ceil(med)

if __name__ == '__main__':
    so = Solution()
    print(so.findMedianSortedArrays([1,3],[2]))
