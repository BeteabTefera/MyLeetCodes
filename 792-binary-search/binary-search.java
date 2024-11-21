class Solution {
    public int search(int[] nums, int target) {
        int low_end = 0;
        int high_end = nums.length - 1;

        System.out.println(high_end);

        while (low_end <= high_end ){
            int mid = (low_end + high_end)/ 2;
            if (nums[mid] == target){
                return mid;
            } 

            if (nums[mid] < target){
                low_end = mid + 1 ;
            } else if (nums[mid] > target) {
                high_end = mid - 1 ;
            } 
        }
        return -1;
    }
}