class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> lc =  new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character s_char = s.charAt(i);
            Character t_char = t.charAt(i);

            lc.putIfAbsent(s_char, 0);
            lc.putIfAbsent(t_char, 0);

            lc.put(s_char, lc.get(s_char)+1);
            lc.put(t_char, lc.get(t_char)-1);
        }
        
        for (Integer v: lc.values()) {
            if (v != 0) {
                return false;
            }
        }

        return true;
    }
}
