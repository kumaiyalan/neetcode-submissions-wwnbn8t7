class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complement = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (complement.containsKey(comp)) {
                int[] res = {complement.get(comp), i};
                return res;
            }
            complement.put(nums[i], i);
        }
        return null;
    }
}
