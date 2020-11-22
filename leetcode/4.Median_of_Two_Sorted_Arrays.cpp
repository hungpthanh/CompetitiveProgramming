class Solution {
public:
    double findMedianSortedArrays_at_K(vector<int>& nums1, int pos1, vector<int>& nums2, int pos2, int k) {
        if (pos1 >= nums1.size()) return nums2[pos2 + k - 1];
        if (pos2 >= nums2.size()) return nums1[pos1 + k - 1];
        vector<int>::iterator up;
        int position;
        double result;
        if (nums2[pos2] > nums1[pos1]) {
            up = upper_bound(nums1.begin() + pos1, nums1.end(), nums2[pos2]);
            if (up == nums1.end()) position = nums1.size() - 1;
            else position = up - nums1.begin() - 1;
            if (k <= position - pos1 + 1) {
                result = nums1[pos1 + k - 1];
                return result;
            }
            else
                return findMedianSortedArrays_at_K(nums1, position + 1, nums2, pos2, k - (position - pos1 + 1));
        }
        else {
                up = upper_bound(nums2.begin() + pos2, nums2.end(), nums1[pos1]);
                if (up == nums2.end()) position = nums2.size() - 1;
                else position = up - nums2.begin() - 1;
                if (k <= position - pos2 + 1) {
                    result = nums2[pos2 + k - 1];
                    return result;
                }
                else return findMedianSortedArrays_at_K(nums1, pos1, nums2, position + 1, k - (position - pos2 + 1));
        }
        return 0;
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int k;
        int l = nums1.size() + nums2.size();
        k = int(l / 2)  + 1;
        if ((nums1.size() + nums2.size()) % 2)
            return findMedianSortedArrays_at_K(nums1, 0, nums2, 0, k);
        else {
            return 0.5 * (findMedianSortedArrays_at_K(nums1, 0, nums2, 0, k - 1 ) + findMedianSortedArrays_at_K(nums1, 0, nums2, 0, k));
        }
    }
};
