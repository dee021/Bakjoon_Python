class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        int idx = 0;
        while (answer <= n && idx < numbers.length){
            answer += numbers[idx];
            idx++;
        }
        return answer;
    }
}