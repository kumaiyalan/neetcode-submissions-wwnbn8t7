class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        Map<Integer, Integer> count = new HashMap<>();
        ArrayList<ArrayList<Integer>> freq = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            freq.add(new ArrayList<>());
        }
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        for (int key : count.keySet()) {
            freq.get(count.get(key)).add(key);
        }
        int index = 0;
        for (int i = nums.length; i > 0; i--) {
            if (freq.get(i).isEmpty()) {
                continue;
            } 
            else {
                for (int j : freq.get(i)) {
                    res[index] = j;
                    index++;
                    if (index == k) {
                        return res;
                    }
                }
            }
        }
        return res;
    }
}
