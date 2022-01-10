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
            String contact[] = in.readLine().trim().split("\\s+");
            String s = in.readLine();
            
            Solution ob = new Solution();
            ArrayList<ArrayList<String>> ans = ob.displayContacts(n, contact, s);
            for(int i = 0;i < ans.size();i++){
                for(int j = 0;j < ans.get(i).size();j++)
                    System.out.print(ans.get(i).get(j) + " ");
                System.out.println();
            }
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution{
    static ArrayList<ArrayList<String>> displayContacts(int n, 
                                        String contact[], String s)
    {
        // code here
        HashSet<String> set = new HashSet<>();
        for (String ele : contact) {
            set.add(ele);
        }
        contact = new String[set.size()];
        int j = 0;
        for (String ele : set) {
            contact[j++] = ele;
        }
        Arrays.sort(contact);
        ArrayList<ArrayList<String>> res = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            res.add(new ArrayList<>());
        }
        
        for (String cont : contact) {
            for (int i = 0; i < cont.length(); i++) {
                if (i < s.length() && s.charAt(i) == cont.charAt(i)) {
                    res.get(i).add(cont);
                } else {
                    break;
                }
            }
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (res.get(i).size() == 0) {
                res.get(i).add("0");
            }
        }
        
        return res;
    }
}