class Solution {
public:
    int reverse(int x) {
        long y=0,z;
        
        while(x!=0)
        {
            z=x%10;
            y=y*10+z;
            x=x/10;
        }
 if(y>INT_MAX || y<INT_MIN) return 0;
 return int(y);
    }
    
};