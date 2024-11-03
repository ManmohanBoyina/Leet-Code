from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left: int, right: int):
            # Base case: if the pointers cross each other, stop recursion
            if left >= right:
                return
            # Swap the elements at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Recursive call with updated pointers
            helper(left + 1, right - 1)
        
        # Start the recursion with the two ends of the list
        helper(0, len(s) - 1)

        


        