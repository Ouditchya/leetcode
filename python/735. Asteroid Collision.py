class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        stack = []
        for i in range(n): 
            if (len(stack) == 0
                or (stack[-1] > 0 and asteroids[i] > 0)
                or (stack[-1] < 0 and asteroids[i] < 0)
                or (stack[-1] < 0 and asteroids[i] > 0)): stack.append(asteroids[i])
            elif (stack[-1] > 0 and asteroids[i] < 0):
                while True:
                    if len(stack) == 0: 
                        stack.append(asteroids[i])
                        break

                    top = stack[-1]
                    
                    if top < 0: 
                        stack.append(asteroids[i])
                        break
                    elif top == abs(asteroids[i]): 
                        stack.pop()
                        break
                    elif top < abs(asteroids[i]): stack.pop()
                    elif top > abs(asteroids[i]): break
            # print(stack)
                
        return stack