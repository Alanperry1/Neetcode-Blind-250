class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(n) - single pass through string where n is length
        # Space Complexity: O(n) - stack can grow up to n/2 elements in worst case
        stack=[]
        valid={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            if c in valid:
                if stack and stack[-1]==valid[c]:
                    stack.pop()
                

            else:
                stack.append(c)
        return True if not stack else False

