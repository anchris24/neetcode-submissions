class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }

        int[] ans = new int[num1.length() + num2.length()];

        // Reverse the strings manually using character indexing
        int n1 = num1.length(), n2 = num2.length();
        for (int i = 0; i < n1; i++) {
            int digit1 = num1.charAt(n1 - 1 - i) - '0';
            for (int j = 0; j < n2; j++) {
                int digit2 = num2.charAt(n2 - 1 - j) - '0';
                int mult = digit1 * digit2 + ans[i + j];
                ans[i + j] = mult % 10;
                ans[i + j + 1] += mult / 10;
            }
        }

        // Find the starting index (skip leading 0s from the back)
        int idx = ans.length - 1;
        while (idx > 0 && ans[idx] == 0) {
            idx--;
        }

        // Build the final string
        String result = "";
        for (int i = idx; i >= 0; i--) {
            result += (char)(ans[i] + '0');
        }

        return result;
    }
}
