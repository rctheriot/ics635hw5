import sys
import math
from datetime import datetime

# ------------------------------------------------------------------------------------------------------------------------

def getLineCountInFile(fileName):
    with open(fileName) as f:
        for lineCount, fileLine in enumerate(f, 1):
            continue
    return lineCount

def getLinesInFileAsArray(fileName):
    lines = []
    with open(fileName) as f:
        for lineCount, fileLine in enumerate(f, 1):
            lines.append(fileLine)
            continue
    return lines


# ------------------------------------------------------------------------------------------------------------------------

def fToStrLimitDecimals(f, decimals=2):
	formatString = "{0:." + str(decimals) + "f}"
	return formatString.format(f)



# ------------------------------------------------------------------------------------------------------------------------

class Blank:
    pass

# ------------------------------------------------------------------------------------------------------------------------


def fileLog(s):
	print("File log>\t", s)
	now = datetime.now()
	dateString = "log-" + str(now.year) + "-"  + str(now.month) + "-"  + str(now.day)
	f = open(dateString + ".log", "a+")
	f.write(str(s) + "\n")
