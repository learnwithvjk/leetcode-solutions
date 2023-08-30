class Solution(object):
    # from collections import deque
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dataSet = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for index, char in enumerate(s):
            if len(stack) > 0 and dataSet[stack[-1]] == char:
                stack.pop()
            elif char in ['(', '[', '{']:
                stack.append(char)
            else:
                return False
        return len(stack) == 0


def getExecutable():
    return Solution().isValid
