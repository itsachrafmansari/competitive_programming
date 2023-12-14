import java.util.HashMap;

class Solution {
    public int maxProduct(int[] nums) {
        HashMap<String, Integer> firstMax = new HashMap<String, Integer>();
        firstMax.put("value", -999999999);
        firstMax.put("index", -1);

        HashMap<String, Integer> secondMax = new HashMap<String, Integer>();
        secondMax.put("value", -999999999);
        secondMax.put("index", -1);

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] > firstMax.get("value")) {
                secondMax.put("value", firstMax.get("value"));
                secondMax.put("index", firstMax.get("index"));
                
                firstMax.put("value", nums[i]);
                firstMax.put("index", i);

            } else if (nums[i] > secondMax.get("value")) {
                secondMax.put("value", nums[i]);
                secondMax.put("index", i);
            }

        }
        
        return (firstMax.get("value") - 1) * (secondMax.get("value") - 1);
    }
}
