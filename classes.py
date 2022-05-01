class test:
    def __init__(self):
        self.navigator = 0
        self.qmap = range(1)
        self.updateTheLists()

    def updateTheLists(self):  # will update rlist,ulist and comments
        self.rlist = self.getTestLen() * ["0"]
        self.ulist = self.getTestLen() * ["0"]
        self.comments = self.getTestLen() * [""]

    def getStart():  # will be used to get first value of the qmap
        return self.qmap[0]

    def getEnd():  # will be used to get the last value of qmap
        return self.qmap[-1]

    def setQMap(self, QuestionMap):  # will be used to define question maps
        self.qmap = QuestionMap
        self.updateTheLists()

    def getNavPos(self):
        return self.navigator

    def resetNav(self):  # reset navigator
        self.navigator = 0

    def islast(self):  # check if navigator is in last possible position
        return self.navigator == self.getTestLen() - 1

    def isFirst(self):  # check if navigator is in first possible position
        return self.navigator == 0

    def nextPos(
        self,
    ):  # goto next pos . return value true means changed position and return value false means unable to change position
        if not self.islast():
            self.navigator += 1
            return True
        return False

    def prevPos(
        self,
    ):  # goto previous pos . return value true means changed position and return value false means unable to change position
        if not self.isFirst():
            self.navigator -= 1
            return True
        return False

    def gotoQ(
        self, Qnumber
    ):  # goto the question,navigator dependent for ease of coding
        if Qnumber >= 0 and Qnumber < self.getTestLen():
            self.navigator = Qnumber
            return True
        return False

    # will check if a question number exists or not
    def checkQnumberExistance(self, Qnumber):
        return Qnumber in self.qmap

    # return navigator value of a question with a specified Qpos value(may have buggy behavior)
    def getQPosNav(self, n=None):
        if n == None:
            n = self.getQPos()

        for i in range(self.getTestLen()):
            if self.qmap[i] == n:
                return i
        else:
            return None

    # return accual number of the current question (or a certain navigator value)
    def getQPos(self, n=None):
        if n == None:
            n = self.navigator
        return self.qmap[n]

    def setRAns(self, val):  # set the right answer for question
        self.rlist[self.navigator] = val

    def setUAns(self, val):  # set users answer for question
        self.ulist[self.navigator] = val

    def getRAns(self, n=None):  # get the right answer for question
        if n == None:
            n = self.navigator
        return self.rlist[n]

    def getUAns(self, n=None):  # get users answer for question
        if n == None:
            n = self.navigator
        return self.ulist[n]

    def getTestLen(self):
        return len(self.qmap)  # return length of test

    def getQstat(
        self, position
    ):  # return current question stats. c for correct , w for wrong , u for unanswered , s for skipped  and e for error
        if self.ulist[position] != "" and self.rlist[position] != "":
            if self.ulist[position] == "0":
                return "u"
            elif self.ulist[position] == "s":
                return "s"
            elif self.ulist[position] == self.rlist[position]:
                return "c"
            else:
                return "w"
        else:
            return "e"

    def getSpecificNumber(self, x):  # function will be used in next functions
        rval = 0
        for i in range(self.getTestLen()):
            if self.getQstat(i) == x:
                rval += 1
        return rval

    def getCorrectNumber(self):
        return self.getSpecificNumber(
            "c"
        )  # returns number of test with correct answers

    def getWrongNumber(self):
        return self.getSpecificNumber(
            "w"
        )  # return total number of wrongly answered questions

    def getUnansweredNumber(self):
        # return total number of unaswered questions
        return self.getSpecificNumber("u")

    def getSkippedNumber(self):
        # return total number of skipped questions
        return self.getSpecificNumber("s")

    # will return the number of wanted questions as a list
    def getSpecificNumbers(self, x):
        rval = 0 * [0]
        pos = 0
        for i in self.qmap:
            if self.getQstat(pos) == x:
                rval += [i]
            pos += 1
        return rval

    def showSpecificQNumbers(self, x):  # function will be used in next functions
        pos = 0
        for i in self.qmap:
            if self.getQstat(pos) == x:
                print(i)
            pos += 1

    def showCorrectQNumbers(self):  # print correctly answered question numbers
        self.showSpecificQNumbers("c")

    def showWrongQNumbers(self):  # print wrongly answered question numbers
        self.showSpecificQNumbers("w")

    def showUnansweredQNumbers(self):  # print unanswered question numbers
        self.showSpecificQNumbers("u")

    def showSkippedQNumbers(self):  # print skipped question numbers
        self.showSpecificQNumbers("s")

    # used for setting comments on a question(current question by default)
    def setComment(self, cmnt, n=None):
        if n == None:
            n = self.navigator
        self.comments[n] = cmnt

    def getComment(self, n=None):  # return the user's comment
        if n == None:
            n = self.navigator
        return self.comments[n]

    # will return navigator values of commented questions
    def getCommentedQuestions(self):
        rlist = 0 * [0]
        for i in range(self.getTestLen()):
            if self.comments[i] != "":
                rlist += [i]
        return rlist

    # the following codes are for suspending to disk (in order to continue at an other time)
    def createSaveDirs():
        import os

        if not os.path.exists("SavedTests/"):
            os.makedirs("SavedTests/")
        if not os.path.exists("SavedAnswerSheets/"):
            os.makedirs("SavedAnswerSheets/")

    def mkSaveString(lst):
        saveString = ""
        for i in range(len(lst)):
            if type(lst[i]) != str:
                saveString += str(lst[i])
            else:
                saveString += lst[i]
            if i != len(lst) - 1:  # if i was not at the last address
                saveString += ","
        return saveString

    def saveToDisk(self, saveFileName):
        test.createSaveDirs()
        saveFile = open("SavedTests/" + saveFileName, "w")
        saveFile.write(test.mkSaveString(list(self.qmap)))
        saveFile.write("\n")
        saveFile.write(test.mkSaveString(self.rlist))
        saveFile.write("\n")
        saveFile.write(test.mkSaveString(self.ulist))
        saveFile.write("\n")
        saveFile.write(test.mkSaveString(self.comments))
        saveFile.write("\n")
        saveFile.write(str(self.navigator))
        saveFile.close()

    def strIntoIntList(inpString):
        returnList = list()
        for i in inpString.split(","):
            returnList += [int(i)]
        return returnList

    def readFromDisk(self, saveFileName):
        test.createSaveDirs()
        saveFile = open("SavedTests/" + saveFileName, "r")
        self.setQMap(test.strIntoIntList(saveFile.readline()))
        self.rlist = saveFile.readline().replace("\n", "").split(",")
        self.ulist = saveFile.readline().replace("\n", "").split(",")
        self.comments = saveFile.readline().replace("\n", "").split(",")
        self.navigator = int(saveFile.readline())

    # the following code is for saving answer sheets (so we dont have to reenter everything manually)
    def mkSavedPart(ansSheetName):
        try:
            ansSheetFile = open("./SavedAnswerSheets/" + ansSheetName, "r+")
            returnList = list()
            for i in ansSheetFile.read().split("\n"):
                if i != "":  # end of line caused some bugs
                    a, b = i.split(":")
                    returnList += [[int(a), b]]
            ansSheetFile.close()
            return returnList
        except FileNotFoundError:
            return [[""]]  # like an empty file

    def saveAnsSheet(self, ansSheetName):
        test.createSaveDirs()

        def mkLivePart():
            returnList = list()
            for i in range(self.getTestLen()):
                returnList += [[self.qmap[i], self.rlist[i]]]
            return returnList

        def sortASheet(part):
            for i in range(len(part) - 1):
                for j in range(i + 1, len(part)):
                    if part[i][0] > part[j][0]:
                        part[i][0], part[j][0] = part[j][0], part[i][0]
            return part

        ##ans sheet storing format
        # [question number]:[question answer] per line
        ## this part will check if some answers overlap or not and after fixing that will merge new answers to the answer sheet (if it exists)
        ## note : recent answers are the priority
        savedPart = test.mkSavedPart(ansSheetName)
        livePart = mkLivePart()
        # now merging and checking for conflicts
        savedPart = sortASheet(savedPart)
        livePart = sortASheet(livePart)
        ### this part does need optimization
        finalPart = list()
        if not savedPart == [""]:
            i = j = 0
            while not (i >= len(livePart) or j >= len(savedPart)):
                if livePart[i][0] <= savedPart[j][0]:
                    finalPart += [livePart[i]]
                    i += 1
                elif savedPart[j][0] < livePart[i][0]:
                    finalPart += [savedPart[j]]
                    j += 1
            finalPart += livePart[i:] + savedPart[j:]
            ##removing dupes
            i = 0
            while not i == len(finalPart) - 1:
                if finalPart[i][0] == finalPart[i + 1][0]:
                    ##remove the additional one(s)
                    del finalPart[i + 1]
                else:
                    i += 1
        else:
            finalPart = livePart
        print(finalPart)
        ## and finally save
        ansSheetFile = open("SavedAnswerSheets/" + ansSheetName, "w")
        for i in finalPart:
            ansSheetFile.write(str(i[0]) + ":" + i[1] + "\n")
        ansSheetFile.close()

    def loadAnsSheet(self, ansSheetName):
        def firstOnesOnly(lst):
            returnList = list()
            for i in lst:
                returnList += [i[0]]
            return returnList

        test.createSaveDirs()
        ##if unable to load a question from file the number of the question will be returned in an array
        returnList = list()
        savedPart = test.mkSavedPart(ansSheetName)
        for i in range(len(self.qmap)):
            if not (self.qmap[i] in firstOnesOnly(savedPart)):
                returnList += [self.qmap[i]]
            else:
                for j in range(len(savedPart)):
                    if self.qmap[i] == savedPart[j][0]:
                        self.rlist[i] = savedPart[j][1]
                        break
        return returnList
