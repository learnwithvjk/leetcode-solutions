
# Analysis:
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxPalindrome = ''
        for index, char in enumerate(s):
            tempPalindrome = getMaxPossiblePalindrome(s, index)
            if len(tempPalindrome) > len(maxPalindrome):
                maxPalindrome = tempPalindrome
        return maxPalindrome

# This method tries to find the maximum possible palindrome by expanding the substring both left an right side.
# Edge Case: "bb" -> for these secnarios when parallely moving left and right we will be going out of the array index thus we have to run the 2nd time for these cases.


def getMaxPossiblePalindrome(s, index):
    if len(s) < 0:
        return ''

    # normal case
    left = index - 1
    right = index + 1
    str1 = s[index]
    while (left >= 0 and right < len(s)):
        if (s[left] == s[right]):
            str1 = s[left] + str1 + s[right]
            left -= 1
            right += 1
        else:
            break

    # edge case
    left = index
    right = index + 1
    str2 = ''
    while (left >= 0 and right < len(s)):
        if (s[left] == s[right]):
            str2 = s[left] + str2 + s[right]
            left -= 1
            right += 1
        else:
            break

    return str1 if len(str1) > len(str2) else str2


def getExecutable():
    return Solution().longestPalindrome
