class Solution:
    def isBalanced(self, num: str) -> bool:
        sum1,sum2=0,0
        count=0
        while int(num)!=0:
            temp=int(num)%10
            if count%2==0:
                sum1+=temp
            else:
                sum2+=temp
            num=str(int(num)//10)
            count+=1
        return True if sum1==sum2 else False
        