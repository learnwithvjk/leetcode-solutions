import os
import importlib
import json
import time
from pathlib import Path

# from python_solutions import Sol_1
# import Sol_2
# import Sol_3
# import Sol_1
# import sys


SOLUTION_DIR = 'python_solutions'
SOLUTION_FILE_NAME = 'Sol_'


def checkIfSolutionExits(solution):
    data_path = os.path.dirname(__file__)
    fileDir = data_path + '/' + SOLUTION_DIR + \
        '/' + SOLUTION_FILE_NAME + solution + '.py'
    solutionPath = Path(fileDir)
    print("Looking at:\n" + fileDir + '\n')
    return solutionPath.exists()


def getSolutionInstance(solution):
    selectedSolutionModulePath = SOLUTION_DIR + \
        '.' + SOLUTION_FILE_NAME + str(solution)
    module = importlib.import_module(selectedSolutionModulePath)
    SolutionClass = module.Solution
    return SolutionClass()


def getTestCases():
    testCasesFile = open('testCases.json')
    testCases = json.load(testCasesFile)
    testCasesFile.close()
    return testCases


def exec(solutionInstance, testCases):
    start_time = time.time()
    for index in range(len(testCases)):
        print("%s%s" % ('test-case-', index))
        print(solutionInstance.longestPalindrome(testCases[index]))

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")


def runTest():

    solution = input('Which solution to run?  ')

    if (not checkIfSolutionExits(solution)):
        print('No solutions match your inputs')
        return

    solutionObj = getSolutionInstance(solution)
    testCases = getTestCases()
    exec(solutionObj, testCases)


runTest()
