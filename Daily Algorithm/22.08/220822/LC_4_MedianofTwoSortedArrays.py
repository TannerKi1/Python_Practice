
nums1 = [1, 2, 3]
nums4 = [1, 3, 5]

def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    mid = (n + m) // 2
    nums3 = nums1 + nums2

    nums3.sort()

    if (n + m) % 2 == 0:
        ans = (nums3[mid - 1] + nums3[mid]) / 2
    else:
        ans = nums3[mid]

    print(ans)


findMedianSortedArrays(nums1, nums4)


