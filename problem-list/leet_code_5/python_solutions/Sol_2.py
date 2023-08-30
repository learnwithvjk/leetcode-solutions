# NOTE: This program will exit in Time Limit Exceeded Exception. Saving this for future reference of algorithms

# Analysis:
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = {}
        return getPalinDromeString(s, cache)

# babsd
#     babs
#         bab
#         abs
#             ab
#                 a
#                 s
#     absd
#         abs
#             ab
#                 a
#                 b
#         bsd
#             bs
#                 b
#                 s
#             sd
#                 s
#                 d


def isPalindrome(s):
    totalIndex = int(len(s)/2)
    for index in range(0, totalIndex):
        index = int(index)
        if s[index] == s[len(s)-1 - index]:
            continue
        else:
            return False
    return True


def getPalinDromeString(s, cache):
    if s in cache:
        return cache[s]
    if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
        return s
    if len(s) == 2:
        return s[0]
    if s[0] == s[len(s)-1] and isPalindrome(s):
        return s

    s1 = getPalinDromeString(s[0:len(s)-1], cache)
    s2 = getPalinDromeString(s[1:len(s)], cache)

    if (len(s1) > len(s2)):
        cache[s] = s1
        return s1
    else:
        cache[s] = s2
        return s2
