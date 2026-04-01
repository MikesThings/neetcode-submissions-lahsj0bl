public class Solution {
    public int Search(int[] nums, int target) {
        int l = 0;
        int r = nums.Length;
        while (l < r) {
            int mid = (r - l)/2 + l;
            if (nums[mid] == target){
                return mid;
            }
            else if (nums[mid] < target) {
                l = mid + 1;
            }
            else {                
                r = mid;
            }
        }
        if (l < nums.Length && nums[l] == target){
            return l;
        }

        return -1;
    }
}
