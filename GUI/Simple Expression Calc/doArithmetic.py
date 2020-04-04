# Evaluate a simple arithmetic expression from a string
from functools import total_ordering
from builtins import str

# Input string to parse
def parseArithmetic(s):
    total = 0.0 # Start with 0.0 sum
    cmd = "+" # We will always add the first value to the total
    dec = False # Boolean value for if we've found a decimal
    tens = 0.1 # For adding decimals
    
    if (len(s) <= 0):
        return "Error: Not a valid expression"
    
    if not(s[0].isnumeric()):
        return "Error: First character must be a number"
    
    bufNum = 0.0 # Buffer for num > 9
    
    for e in s:
        if (e.isnumeric()):
            if (dec):
                bufNum = bufNum + float(e)*tens
                tens = tens * 0.1
            else:
                bufNum = bufNum * 10 + float(e)
        elif (e == "."):
            dec = True
        else:
            total = doArithemetic(total, bufNum, cmd)
            cmd = e
            bufNum = 0.0
            tens = 0.1
            dec = False

    total = doArithemetic(total, bufNum, cmd)
    return total

def doArithemetic(total, bufNum, op):
    #print(str(total) + " " + str(op) + " " + str(bufNum))
    if (op == "+"):
        return total + bufNum
    elif (op == "-"):
        return total - bufNum
    elif (op == "*"):
        return total * bufNum
    elif (op == "/"):
        return total / bufNum
