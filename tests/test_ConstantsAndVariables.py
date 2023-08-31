from blankquestions.ConstantsVariables import *
from solutions.AssignmentSolutions import constantsAndVariables as constantsAndVariablesAnswer

def testConstantsAndVariables():
    assert constantsAndVariables() == 23

def testconstantsAndVariablesSolution():
    assert constantsAndVariablesAnswer() == 23

def testNumTimesQuoteIn23():
    assert numTimesQuoteIn23() == 15

def testStartAndEndIndeciesOfSubstring():
    assert startAndEndIndicesOfSubString() == (262, 308)

def testIntegerSeqToString():
    assert integerSeqToString() == "J Robert Oppenheimer"