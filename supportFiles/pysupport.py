import sys
import math
from datetime import datetime


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

class Blank:
    pass

# ------------------------------------------------------------------------------------------------------------------------

def addLineToFile(fileName, string):
    with open(fileName, 'a') as file:
        file.write(string + "\n")
# ------------------------------------------------------------------------------------------------------------------------

def addTextToFile(fileName, string):
    with open(fileName, 'a') as file:
        file.write(string)

# ------------------------------------------------------------------------------------------------------------------------


def fileLog(s):
	print("File log>\t", s)
	now = datetime.now()
	dateString = "log-" + str(now.year) + "-"  + str(now.month) + "-"  + str(now.day)
	f = open(dateString + ".log", "a+")
	f.write(str(s) + "\n")
