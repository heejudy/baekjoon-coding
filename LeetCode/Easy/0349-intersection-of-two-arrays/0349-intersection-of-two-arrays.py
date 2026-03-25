class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set 으로 해서 둘을 빼면 -> 겹치지 않는 것 -> 큰 거 - 겹치지 않는 거
        set_1 = set(nums1)
        set_2 = set(nums2)
        set_total = set(nums1 + nums2)
        not_intersection = list(set_1 - set_2) + list(set_2 - set_1)

        return list(set_total - set(not_intersection))