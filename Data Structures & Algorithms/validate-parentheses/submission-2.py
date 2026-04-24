class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        left = ["(", "[", "{"]

        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ")":
                    if stack.pop() != "(":
                        return False
                elif c == "]":
                    if stack.pop() != "[":
                        return False
                elif c == "}":
                    if stack.pop() != "{":
                        return False
                

        if not stack:
            return True
        else:
            return False