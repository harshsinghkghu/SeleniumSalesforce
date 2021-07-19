from TestCases import TestCases


def runTest():
    testCase = TestCases()
    testCase.siteTest(testCase.openBrowser())


if __name__ == '__main__':
    runTest()
