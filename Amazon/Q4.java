// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            int n = Integer.parseInt(in.readLine());
            String a[] = in.readLine().trim().split("\\s+");
            int p[] = new int[n];
            for(int i = 0;i < n;i++)
                p[i] = Integer.parseInt(a[i]);
            
            Solution ob = new Solution();
            System.out.println(ob.matrixChainOrder(p, n));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution{
    static String st="";
    static char name;
    
    static void printParenthesis(int i, int j, int n, int[][] bp){
    	if (i == j){
    		st += name;
    		name++;
    		return;
    	}
    	st += '(';
    	printParenthesis(i, bp[i][j], n,bp);
    	printParenthesis(bp[i][j] + 1, j,n, bp);
    	st += ')';
    }
    
    static String matrixChainOrder(int p[], int n){
        // code here
        int dp[][]=new int[n][n];
    	int bp[][]=new int[n][n];
    	for (int i = 1; i < n; i++)
    	    dp[i][i] = 0;
    	for (int L = 2; L < n; L++){
    		for (int i = 1; i < n-L+1; i++){
    			int j = i+L-1;
    			dp[i][j] = Integer.MAX_VALUE;
    			for (int k = i; k <= j-1; k++){
    				int q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j];
    				if (q < dp[i][j]){
    					dp[i][j] = q;
    					bp[i][j] = k;
    				}
    			}
    		}
    	}
    	name = 'A';
    	printParenthesis(1, n-1, n, bp);
    	return st;
    }
}



