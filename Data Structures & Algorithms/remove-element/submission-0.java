class Solution {
    public int removeElement(int[] nums, int val) {
        int start = 0;
        int end = nums.length;
        
        while (start < end) {
            if (nums[start] == val) {
                nums[start] = nums[--end];
            } else {
                start++;
            }

        }

        return end;
    }
}