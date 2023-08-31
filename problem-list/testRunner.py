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


def getService():
    service = int(input('Choose service:\n1.Leet Code'))
    if (service == 1):
        return 'leet_code'
    return ''


def getProblemFolderName(service, problem):
    return service + '_' + problem


SOLUTION_DIR = 'python_solutions'
SOLUTION_FILE_NAME = 'Sol_'


def checkIfSolutionExits(solution, service, problem):
    data_path = os.path.dirname(__file__)
    serviceName = getProblemFolderName(service, problem)
    fileDir = data_path + '/' + serviceName + '/' + SOLUTION_DIR + \
        '/' + SOLUTION_FILE_NAME + solution + '.py'
    solutionPath = Path(fileDir)
    print("Looking at:\n" + fileDir + '\n')
    return solutionPath.exists()


def getRunMethod(solution, service, problem):
    serviceName = getProblemFolderName(service, problem)
    selectedSolutionModulePath = serviceName + '.' + SOLUTION_DIR + \
        '.' + SOLUTION_FILE_NAME + str(solution)
    module = importlib.import_module(selectedSolutionModulePath)
    return module.getExecutable


def getTestCases(service, problem):
    serviceName = getProblemFolderName(service, problem)
    testCasesFile = open(serviceName + '/testCases.json')
    testCases = json.load(testCasesFile)
    testCasesFile.close()
    return testCases


def exec(runMethod, testCases):
    start_time = time.time()
    for index in range(len(testCases)):
        print("%s%s" % ('test-case-', index))
        params = testCases[index]
        print(runMethod(*params))

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")


def runTest():
    service = getService()
    problem = input('Which problem to run?  ')
    solution = input('Which solution to execute?  ')

    if (not checkIfSolutionExits(solution, service, problem)):
        print('No solutions match your inputs')
        return

    runMethod = getRunMethod(solution, service, problem)
    testCases = getTestCases(service, problem)
    exec(runMethod, testCases)


runTest()
