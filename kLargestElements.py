#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:53:49 2020

@author: clarke homan  (cahoman@gmail.com)

Given an array of N positive integers, print k largest elements from the array.
The output elements should be printed in decreasing order.

Input:
  The first line of input contains an integer T denoting the number of test
  cases.

  The first line of each test case is N and K, N is the size of array and K
  is the number of largest elements to be returned.

  The second line of each test case contains N input C[i].

Output:
  Print the k largest element in descending order.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
K ≤ N
-10000 ≤ C[i] ≤ 10000

Example:
Input:
2
5 2
12 5 787 1 23
7 3
1 23 12 9 30 2 50

Output:
787 23
50 30 23

Although this implementation is not the most succinct, it does utilize the
following Python and programming concepts:
    - Opening a text data file that contains the test cases
    - Can handle any number of test cases sets found within the text data file
    - Use of object oriented programming with data protection provided by
      class
    - Utilizes list
    - Utilizes DataFrame to contain a set of test cases with variable number
      set size


"""
import pandas as pd


DATAFILE = 'kLargestElement.dat'

# --- HELPER CODE ---


class largestElements(object):
    """class largestElements."""

    def __init__(self, numTestCases, fileHandle):
        """
        Initialize a largestElements object.

        Reads a set of test cases and
        stores the test cases into a DataFrame. Each row is a test case.
        The columns are the ArraySize which is the number of elements within
        a test case number array. The second column is the number of largest
        elements to select from the test case number array. The third column
        is the number array itself for the testcase.

        numTestCases (int): number of test cases to process
        fileHandle (file): file handle to test cases

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list,

                              determined using helper function load_words)

        Args:
            numTestCases (int): DESCRIPTION.
            fileHandle (fileHandle): file handle to test case data file
        ___
        Returns None.
        ___
        """
        self.numTestCases = numTestCases
        for i in range(numTestCases):
            sizeandelements = fileHandle.readline()
            arraySize, numTopElements = sizeandelements.split()
            arraySize = int(arraySize)
            numTopElements = int(numTopElements)
            numArray = fileHandle.readline()
            numArray = numArray.split()
            numarray = []
            for j in numArray:
                numarray.append(int(j))
            numarray.sort(reverse=True)
            testCase = [[arraySize, numTopElements, numarray]]
            if i < 1:
                self.df = pd.DataFrame(testCase,
                                       columns=['ArraySize',
                                                'NumTopElements',
                                                'Series'])
            else:
                dfTemp = pd.DataFrame(testCase,
                                      columns=['ArraySize',
                                               'NumTopElements',
                                               'Series'])
                self.df = self.df.append(dfTemp)

    def getTopElements(self, testCaseIndex):
        """
        Retrieve the top N values of an indexed test case.

        N is a column of the test case. Assumes the test case number array
        has been presorted in decending values.

        Args:
            testCaseIndex (int): Indexes which test case to retrieve top values
            from.

        Returns
            string of top values from test case

        """
        assert testCaseIndex < self.numTestCases, 'testCaseIndex too great'

        resultsString = ''
        numArray = self.df.iloc[testCaseIndex].Series
        for i in range(self.df.iloc[testCaseIndex].NumTopElements):
            resultsString += str(numArray[i]) + ' '
        return resultsString

if __name__ == '__main__':
    numTestCases = 0
    print("Loading testcases from file...\n")
    inFile = open(DATAFILE, 'r')

    while True:
        nextSetStr = inFile.readline()
        if nextSetStr == '':
            break
        numTestCases = int(nextSetStr)

        print('New set of test cases. Num test cases:', str(numTestCases))
        testcase = largestElements(numTestCases, inFile)

        for i in range(numTestCases):
            results = testcase.getTopElements(i)
            print('Test case', i, ':', results)
        print('\n')
            
    print('Completed parsing datafile. Goodbye!')
