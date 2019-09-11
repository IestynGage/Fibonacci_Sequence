import time

def fibonacciDP(sequenceNumber):
    """
    A Dynamic Programming Algorithm that gets a number from fibonacci sequence at certain point in sequence.

    Args:
        sequenceNumber {integer} the place in the sequence to get the number from
    Return:
        {integer} the number from fibonacci sequence
    """
    if(sequenceNumber<0):
        return 0

    if(sequenceNumber<2):
        return 1

    sequenceList = [None] * sequenceNumber
    sequenceList[0] = 1
    sequenceList[1] = 1

    for x in range (2,sequenceNumber):
        sequenceList[x] = sequenceList[x-1] + sequenceList[x-2]

    return sequenceList[sequenceNumber-1]


def fibonacciRecursion(sequenceNumber):
    """
    A recursive Algorithm that gets a number from fibonacci sequence at certain point in sequence

    Args:
        sequenceNumber {integer} the place in the sequence to get the number from
    Return:
        {integer} the number from fibonacci sequence
    """
    if(sequenceNumber<0):
        return 0

    if(sequenceNumber<2):
        return 1
    else:
        previousNumb = (fibonacciRecursion(sequenceNumber-1))
        secondPreviousNumb = (fibonacciRecursion(sequenceNumber-2))

        return previousNumb + secondPreviousNumb


def timeComparison(testNumber):
    """
    This function compares the time it takes to get number from fibonacci sequence. The
    higher the testNumber, the more time it takes to compute both function.

    Args:
        testNumber {integer} The number to get from Sequence to test speed
    """

    dpStart = time.clock()
    fibonacciDP(testNumber)
    dpEnd = time.clock()

    dpTime = dpEnd - dpStart

    recursionStart = time.clock()
    fibonacciRecursion(testNumber)
    recursionEnd = time.clock()

    recursionTime = recursionEnd - recursionStart

    print(" \n----------------------------------------------------")
    print("The Dynamic Programming technique took {0:10.8f} seconds to solve problem".format((dpTime)))
    print("The Recursion technique took {0:10.8f} seconds to solve problem".format((recursionTime)))
    print("----------------------------------------------------")

