class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        counter = {}
        for char in word:
            try:
                counter[char] += 1
            except:
                counter[char] = 1
        tempDict = {}
        tempKey = None
        for key in counter:
            tempKey = counter[key]
            try:
                tempDict[counter[key]].append(key)
            except:
                tempDict[counter[key]] = [key]

        if len(tempDict) == 1:
            try:
                if len(tempDict[tempKey]) == 1 or tempKey == 1:
                    return True
            except:
                return False

        if len(tempDict) == 2:
            minCount = 101  # since word count wont exceed 100
            maxCount = -1  # since count cant be negative
            for key in tempDict:
                minCount = min(minCount, key)
                maxCount = max(maxCount, key)

            if minCount == 1 and len(tempDict[minCount]) == 1 or (maxCount - minCount == 1 and len(tempDict[maxCount]) == 1):
                return True

        return False


def getExecutable(*args):
    return Solution().equalFrequency(*args)
