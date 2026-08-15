class Solution {
    public static int[] sort(int[] sorted) {
        int n = sorted.length;
        int temp = 0;
        // insertion sort
        for (int i = 0; i <= n - 2; i++) {
            for (int j = i + 1; j > 0; j--) {
                if (sorted[j - 1] > sorted[j]) {
                    temp = sorted[j];
                    sorted[j] = sorted[j - 1];
                    sorted[j - 1] = temp;
                } else {
                    break;
                }
            }
        }
        // for (int i : sorted) {
        // System.out.println(i);
        // }
        return sorted;
    }
    public boolean isAnagram(String s, String t) {
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        // List<Integer>IntSList=new ArrayList<>();
        // List<Integer>IntTList=new ArrayList<>();
        int[] IntSList = new int[sArr.length];
        int[] IntTList = new int[tArr.length];
        for (int i = 0; i < sArr.length; i++) {
            IntSList[i] = (int) sArr[i];
            // System.out.println(IntSList[i]);
        }
        for (int i = 0; i < tArr.length; i++) {
            IntTList[i] = (int) tArr[i];
        }
        if (Arrays.equals(sort(IntSList), sort(IntTList))) {
            return true;
        } else {
            return false;
        }
    }
}

