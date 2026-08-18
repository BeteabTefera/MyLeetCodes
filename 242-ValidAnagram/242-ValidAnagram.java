// Last updated: 8/18/2026, 2:50:01 PM
class Solution {
    public boolean isAnagram(String s, String t) {
        char [] sChars = s.toCharArray();
        char [] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}