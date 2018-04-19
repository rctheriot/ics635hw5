import sys
import math


# ------------------------------------------------------------------------------------------------------------------------

def getLinesInFile(fileName):
    with open(fileName) as f:
        for lineCount, fileLine in enumerate(f, 1):
            continue
    return lineCount



# ------------------------------------------------------------------------------------------------------------------------

def fToStrLimitDecimals(f, decimals=2):
	formatString = "{0:." + str(decimals) + "f}"
	return formatString.format(f)



# ------------------------------------------------------------------------------------------------------------------------

class blank:
    pass

# ------------------------------------------------------------------------------------------------------------------------

def addLineToFile(fileName, string):
    with open(fileName, 'a') as file:
        file.write(string + "\n")
# ------------------------------------------------------------------------------------------------------------------------

def addTextToFile(fileName, string):
    with open(fileName, 'a') as file:
        file.write(string)