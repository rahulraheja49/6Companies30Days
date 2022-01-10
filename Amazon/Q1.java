// { Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader in =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while (t-- > 0) {
            int K = Integer.parseInt(in.readLine());
            int N = Integer.parseInt(in.readLine());
            String input_line[] = in.readLine().trim().split("\\s+");
            int A[] = new int[N];
            for (int i = 0; i < N; i++) A[i] = Integer.parseInt(input_line[i]);

            Solution ob = new Solution();
            System.out.println(ob.maxProfit(K, N, A));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    static int maxProfit(int K, int N, int A[]) {
        // code here
        int dp[][]=new int[K+1][N];
        int max_so=Integer.MIN_VALUE;
        for(int i=1;i<=K;i++) {
            max_so=Integer.MIN_VALUE;
            for(int j=1;j<N;j++) {
                max_so=Math.max(max_so,dp[i-1][j-1]-A[j-1]);
                dp[i][j]=Math.max(dp[i][j-1],max_so+A[j]);
            }
        }
        return dp[K][N-1];
    }
}