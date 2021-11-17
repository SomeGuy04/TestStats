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
        navigator=0
        self.start=start
        self.end=end
        self.step=step
        qpos=start
        testlen=len(range(start,end,step))
        rlist=testlen*[0]
        ulist=testlen*[0]
    def getNavPos(self):
        return(navigator)
    def islast(self):   #check if navigator is in last possible position
        if(navigator==testlen-1):
            return True
        return False
    def isFirst(Self):  #check if navigato is in first possible position
        if(navigator==0):
            return True
        return False
    def nextPos(self):  #goto next pos . return value true means changed position and return value false means unable to change position
        if not islast(self):
            navigator+=1
            qpos+=step
            return True
        return False
    def prevPos(self):  #goto previous pos . return value true means changed position and return value false means unable to change position
        if not isFirst(self):
            navigator-=1
            qpos-=step
            return True
        return False
    def setRAns(self,val):  #set the right answer for question 
        rlist[navigator]=val
    def setUAns(self,val):  #set users answer for question 
        ulist[navigator]=val
    def getQstat(self,position=navigator):     #return current question stats. c for correct , w for wrong , u for unanswered , s for skipped  and e for error
        if(ulist[position]!='' and rlist[position]!=''):
            if (ulist[position]=='0'):
                return 'u'
            elif ulist[position]=='s':
                return 's'
            elif ulist[position]==rlist[position]:
                return 'c'
            else:
                return 'w'
        else:
            return 'e'
    def getCorrectNumber(self): #returns number of test with correct answers
        rval=0
        for i in range(testlen):
            if(getQstat(self,i)=='c'):
                rval+=1
        return rval
    def getWrongNumber(self):   #return total number of wrongly answered questions
        rval=0
        for i in range(testlen):
            if(getQstat(self,i)=='w'):
                rval+=1
        return rval
    def getUnansweredNumber(self):  #return total number of unaswered questions
        rval=0
        for i in range(testlen):
            if(getQstat(self,i)=='u'):
                rval+=1
        return rval
    def getSkippedNumber(self):     #return total number of skipped questions
        rval=0
        for i in range(testlen):
            if(getQstat(self,i)=='s'):
                rval+=1
        return rval
    def showCorrectQNumbers(self):  #print correctly answered question numbers
        rval=0
        pos=0
        for i in range(start,end,step):
            if(getQstat(self,pos)=='c'):
                print(i)
            pos+=1
        return rval
    def showWrongQNumbers(self):    #print wrongly answered question numbers
        rval=0
        pos=0
        for i in range(start,end,step):
            if(getQstat(self,pos)=='w'):
                print(i)
            pos+=1
        return rval
    def showUnansweredQNumbers(self):   #print unanswered question numbers
        rval=0
        pos=0
        for i in range(start,end,step):
            if(getQstat(self,pos)=='u'):
                print(i)
            pos+=1
        return rval
    def showSkippedQNumbers(self):  #print skipped question numbers
        rval=0
        pos=0
        for i in range(start,end,step):
            if(getQstat(self,pos)=='s'):
                print(i)
            pos+=1
        return rval