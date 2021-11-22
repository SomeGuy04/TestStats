class test:
    start=1
    end=2
    step=1
    rlist=[0] # list of right answers
    ulist=[0] # list of user answers
    navigator=0 #int used for navigating in jumps(in-list number of the question)
    qpos=0 #actual number of the question
    testlen=1
    def __init__(self,start=1,end=2,step=1):
        self.navigator=0
        self.start=start
        self.end=end+1  #for making the last question availale in test
        self.step=step
        self.qpos=start
        self.testlen=len(range(start,end+1,step))
        self.qmap=range(start,end+1,step)
        self.rlist=self.testlen*[0]
        self.ulist=self.testlen*[0]
    def getNavPos(self):
        return(self.navigator)
    def resetNav(self): #reset navigator
        self.qpos=self.start
        self.navigator=0
    def islast(self):   #check if navigator is in last possible position
        if(self.navigator==self.testlen-1):
            return True
        return False
    def isFirst(Self):  #check if navigato is in first possible position
        if(self.navigator==0):
            return True
        return False
    def nextPos(self):  #goto next pos . return value true means changed position and return value false means unable to change position
        if not self.islast():
            self.navigator+=1
            self.qpos+=self.step
            return True
        return False
    def prevPos(self):  #goto previous pos . return value true means changed position and return value false means unable to change position
        if not self.isFirst():
            self.navigator-=1
            self.qpos-=self.step
            return True
        return False
    def setRAns(self,val):  #set the right answer for question 
        self.rlist[self.navigator]=val
    def setUAns(self,val):  #set users answer for question 
        self.ulist[self.navigator]=val
    def getQPos(self):      #return accual number of the current question
        return self.qpos
    def getTestLen(self):   #return length of test
        return self.testlen
    def getQstat(self,position):     #return current question stats. c for correct , w for wrong , u for unanswered , s for skipped  and e for error
        if(self.ulist[position]!='' and self.rlist[position]!=''):
            if (self.ulist[position]=='0'):
                return 'u'
            elif self.ulist[position]=='s':
                return 's'
            elif self.ulist[position]==self.rlist[position]:
                return 'c'
            else:
                return 'w'
        else:
            return 'e'
    def getSpecificNumber(self,x):  #function will be used in next functions
        rval=0
        for i in range(self.testlen):
            if(self.getQstat(i)==x):
                rval+=1
        return rval
    def getCorrectNumber(self): #returns number of test with correct answers
        return self.getSpecificNumber('c')
    def getWrongNumber(self):   #return total number of wrongly answered questions
        return self.getSpecificNumber('w')
    def getUnansweredNumber(self):  #return total number of unaswered questions
        return self.getSpecificNumber('u')
    def getSkippedNumber(self):     #return total number of skipped questions
        return self.getSpecificNumber('s')
    def showSpecificQNumbers(self,x): #function will be used in next functions
        pos=0
        for i in self.qmap:
            if(self.getQstat(pos)==x):
                print(i)
            pos+=1
    def showCorrectQNumbers(self):  #print correctly answered question numbers
        self.showSpecificQNumbers('c')
    def showWrongQNumbers(self):    #print wrongly answered question numbers
        self.showSpecificQNumbers('w')
    def showUnansweredQNumbers(self):   #print unanswered question numbers
        self.showSpecificQNumbers('u')
    def showSkippedQNumbers(self):  #print skipped question numbers
        self.showSpecificQNumbers('s')