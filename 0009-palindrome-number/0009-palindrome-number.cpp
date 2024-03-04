class Solution {
public:
    bool isPalindrome(int x) {

        long y=0,z,n;
         n=x;
        while(x!=0)
        {
            z=x%10;
            y=y*10+z;
            x=x/10;
        }
if(n!=y || y<0) return false;
 return true;
    }
    
};