class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length%n == 0?num_list.length/n:num_list.length/n + 1];
        for (int i = 0;i*n < num_list.length; i++)
            answer[i] = num_list[i*n];
        return answer;
    }
}