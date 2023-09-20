from blankquestions.ConstantsVariables import *

def testConstantsAndVariables():
    assert constantsAndVariables() == 66-43

def testNumTimesQuoteIn23():
    assert numTimesQuoteIn23() == 27-12

def testStartAndEndIndeciesOfSubstring():
    assert startAndEndIndicesOfSubString() == (266-4, 310-2)

def testIntegerSeqToString():
    assert integerSeqToString() == (bytes.fromhex('4a20526f62657274204f7070656e6865696d6572').decode('utf-8'))