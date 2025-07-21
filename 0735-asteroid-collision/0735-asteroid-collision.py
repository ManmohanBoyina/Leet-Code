class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for aster in asteroids:
            while stack and aster<0<stack[-1]:
                if stack[-1]<-aster:
                    stack.pop()
                    continue
                elif stack[-1]==-aster:
                    stack.pop()
                break
            else:
                stack.append(aster)
        return stack
