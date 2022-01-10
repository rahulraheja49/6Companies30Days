// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-->0){
            String s1[] = in.readLine().trim().split("\\s+");
            int mat[][] = new int[9][9];
            for(int i = 0;i < 81;i++)
                mat[i/9][i%9] = Integer.parseInt(s1[i]);
            
            Solution ob = new Solution();
            System.out.println(ob.isValid(mat));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution{
    static int isValid(int mat[][]){
        // code here
        int n=9;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                if (!isValidConfig(mat, i, j))
                     return 0;
        return 1;
    }
    
    public static boolean isValidConfig(int arr[][], int row, int col){
        return notInRow(arr, row) && notInCol(arr, col) && notInBox(arr, row - row % 3, col - col % 3);
    }
    
    public static boolean notInBox(int arr[][], int startRow, int startCol){
        HashSet<Integer> st = new HashSet<>();
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 3; col++){
                int curr = arr[row + startRow][col + startCol];
                if (st.contains(curr)) return false;
                if (curr != 0) st.add(curr);
             }
         }
         return true;
    }
    
    public static boolean notInCol(int arr[][], int col){
        HashSet<Integer> st = new HashSet<>();
        for(int i = 0; i < 9; i++){
            if (st.contains(arr[i][col]))
                return false;
            if (arr[i][col] != 0)
                st.add(arr[i][col]);
        }
        return true;
    }
    
    public static boolean notInRow(int arr[][], int row){
        HashSet<Integer> st = new HashSet<>();
        for(int i = 0; i < 9; i++){
            if (st.contains(arr[row][i]))
                return false;
            if (arr[row][i] != 0)
                st.add(arr[row][i]);
        }
        return true;
    }
}