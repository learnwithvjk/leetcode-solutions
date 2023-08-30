# NOTE: This program will exit in Time Limit Exceeded Exception. Saving this for future reference of algorithms

# Analysis:
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        maxString = ""
        # and index-len(s) > len(maxString)
        # and innerIndex-len(s) > len(maxString)
        while (index < len(s) and len(s) - index > len(maxString)):
            innerIndex = index
            tempString = ''
            while (innerIndex < len(s)):
                tempString += s[innerIndex]
                reversedString = "".join(reversed(tempString))
                if tempString == reversedString and len(tempString) > len(maxString):
                    maxString = tempString
                innerIndex += 1
            index += 1
        return maxString


def getExecutable():
    return Solution().longestPalindrome
